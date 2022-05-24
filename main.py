from CellGroupNumbersTool import *

# Main function here
if __name__ == '__main__':

    # Read file
    try:
        raw_data_sabbath = input('輸入主日出席名單(名字以空格分開)\n')
        raw_data_cell = input('輸入小組出席名單(名字以空格分開)\n')
    except EOFError:
        pass

    # Preprocess data
    list_sabbath = raw_data_sabbath.split(' ')
    list_cell = raw_data_cell.split(' ')
