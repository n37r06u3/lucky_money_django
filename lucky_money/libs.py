from decimal import Decimal, InvalidOperation  
                    
import random  
                    
                    
def money_val(min, max):  
    return min if min > max else Decimal(str(random.randint(min, max)))  
                    
                    
def money_random(total, num, min=0.01):  
    """ 
    :param total=10; # 红包总额 10 元 
    :param num=8; # 分成 8 个红包，支持 8 人随机领取 
    :param min=0.01; # 每个人最少能收到 0.01 元 
    """  
    money_list = []  
                    
    try:  
        total = Decimal(str(total))  
    except InvalidOperation as e:  
        return money_list, e
    try:
        if isinstance(num, float) and int(num) != num:  
            raise ValueError(u'Invalid value for Num: \'{0}\''.format(num))  
        num = Decimal(str(int(num)))
    except ValueError as e:  
        return money_list, e
    try:
        min = Decimal(str(min))  
    except InvalidOperation as e:  
        return money_list, e
    if total < num * min:
        return money_list, u'Invalid value for Total-{0}, Num-{1}, Min-{2}'.format(total, num, min)  

    for i in range(1, int(num)):
        safe_total = (total - (num - i) * min) / (num - i)  # 随机安全上限  
        money = money_val(min * 100, int(safe_total * 100)) / 100  
        total -= money  
        money_list.append(money)
    money_list.append(total)
                    
    random.shuffle(money_list)  # 随机打乱  
                    
    return money_list
                    
                    
if __name__ == '__main__':  
    print(money_random(5, 4))
    print(sum(money_random(5, 4)))