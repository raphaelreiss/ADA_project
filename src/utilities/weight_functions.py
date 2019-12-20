import re
import pickle
from IPython.core.debugger import set_trace
import numpy as np
def create_single_weights(df,unit):
    """
    iterate over the items whose unit is CT and return a list of their corresponding weights using user interaction.
    df: dataframe containingCOMMODITY_DESC and SUB_COMMODITY_DESC columns"""
    print('Start of create_single_weights!')
    if unit == 'space':
        temp = df[df.CURR_SIZE_OF_PRODUCT == ' '][['COMMODITY_DESC','SUB_COMMODITY_DESC','CURR_SIZE_OF_PRODUCT']].copy()
    else:
        temp = df[df.CURR_SIZE_OF_PRODUCT.str.contains(unit)][['dunn_name','CURR_SIZE_OF_PRODUCT']].copy()
    temp.rename(columns = {'CURR_SIZE_OF_PRODUCT':'single_weight'},inplace = True)
    temp['single_weight'] = 1
    
    single_weights_df = {}
    L = temp.shape[0]
    for k,(index, row) in enumerate(temp.iterrows()):
        print('%i / %i '  % (k,L))
        fail = True
        while fail:
            print(row.desc)
            try:
                q = float(input('Input:'))
                fail = False
            except ValueError:
                print("Not a number")
        single_weights_df[index] = q
    print('Operation terminated!')
    with open('../saved_data/'+ unit +'_articles.pickle', 'wb') as file:
        pickle.dump(single_weights_df, file, protocol=pickle.HIGHEST_PROTOCOL)
    return single_weights_df


def start_create_single_weights(string,df):
    try:
        with open('../saved_data/'+ string +'_articles.pickle', 'rb') as file:
            single_weights = pickle.load(file)
            print('Successful read.')
    except IOError:
            single_weights = create_single_weights(df,string)
    return single_weights

def get_weight(word:str):
    """
    extract the quantity of the string if the unit present in the string is present in the array of the function
    word: string like 'dumbinfo 12 PK/34 OZ' 
    """
    word = word.upper()
    empt = re.compile('^\s*$')
    if empt.match(word):
        return np.nan
    
    def search(units,word):
        """
        units: list of strings corresponding to the same unit (ex 'LT' and 'LITER')
        """
        string = '|'.join(units)
        pattern = '^.*?([0-9]*\.?[0-9]*)\s*(?:' + string + ').*$'
        #recall: ?: in a group makes the parenthesis non capturing
        #*? is a lazy matching (non agressive)
        return re.search(pattern,word)
    
    def test(units,cstt,word = word):
        """
        units: list of strings corresponding to the same unit (ex 'LT' and 'LITER')
        cstt: constant allowing to obtain kilos from this particular unit
        """
        se = search(units,word)
        if se:
            if se.group(1) == '':
                #writing just LITER is one liter
                return (True,cstt)
            return(True,float(se.group(1))* cstt)
        return (False,0)
    
    units = [(['OZ','OUNCE'],0.0283495),\
             (['LB'],0.453592),\
             (['GA'],3.78541 ),\
             (['DZ'],12 * 0.05),\
             (['PK'],0.33),\
             (['LT','LITER','LTR'],1),\
             (['ML'], 0.001),\
             (['PT','PINT'],0.473176473),\
             (['QT'],np.nan),\
             (['CT'],np.nan),
             (['QUART'],0.9463529)]
    
    for i in units:
        res = test(*i)
        if res[0]:
            return res[1]
        
    raise AssertionError('pas trouvé')
    
