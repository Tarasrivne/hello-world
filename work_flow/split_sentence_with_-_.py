a = ['django chto  eto takoe    poryadok ustanovki'
'model mtv   marshrutizaciya funkcii  predstavleniya'
'marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya']
for word in a:
    word_split = word.split() #"""rosbuvae stroky"""
    word_join = '-'.join(word_split) #"""obyednye stroky with -  """
    print(word_join)