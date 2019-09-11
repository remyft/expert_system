def deal_parse(left, right, mid):
    if (mid == "=>"):
        parse(left, right)
    else:
        parse(left, right)
        parse(right, left)
    
