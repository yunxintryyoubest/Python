



def get_all_conpon(obj):
    '''
    全局的优惠卷信息
    :param obj:
    :param conpon_dic_name:
    :return:
    '''
    conpon_dic_name={}
    conpon_id = obj.pk
    conpon_dic_name[conpon_id] = {
        '全局优惠卷编号': obj.pk,
        'type': obj.coupon.get_coupon_type_display(),
        'coupon_name': obj.coupon.coupon_name,
    }
    if obj.coupon.coupon_type == 1:  ##全品卷
        conpon_dic_name[conpon_id].update({
            'money_equal_value': obj.coupon.money_equal_value
        })
    elif obj.coupon.coupon_type == 2:  ##满减卷
        conpon_dic_name[conpon_id].update({
            'minimum_consume': obj.coupon.minimum_consume,
            'money_equal_value': obj.coupon.money_equal_value
        })
    elif obj.coupon.coupon_type == 3:  ##折扣卷
        conpon_dic_name[conpon_id].update({
            'off_percent': obj.coupon.off_percent
        })
    return conpon_dic_name





def  get_course_conpon(course_obj):

    '''
    课程的优惠卷信息

    :param course_obj:
    :return:
    '''
    conpon_type = {
        '局部优惠卷编号': course_obj.coupon.pk,
        'type': course_obj.coupon.get_coupon_type_display(),
        'coupon_name': course_obj.coupon.coupon_name,
    }
    if course_obj.coupon.coupon_type == 1:  ##全品卷
        conpon_type.update({
            'money_equal_value': course_obj.coupon.money_equal_value
        })
    elif course_obj.coupon.coupon_type == 2:  ##满减卷
        conpon_type.update({
            'minimum_consume': course_obj.coupon.minimum_consume,
            'money_equal_value': course_obj.coupon.money_equal_value
        })
    elif course_obj.coupon.coupon_type == 3:  ##折扣卷
        conpon_type.update({
            'off_percent': course_obj.coupon.off_percent
        })

    return   conpon_type