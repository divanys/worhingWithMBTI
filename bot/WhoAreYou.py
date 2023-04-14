def who_are_you(results):
    personality_type = ""

    if results[::7].count(1) > results[::7].count(0):
        e_i_max = results[::7].count(1)
        personality_type += "E"
    else:
        e_i_max = results[::7].count(0)
        personality_type += "I"

    ei = e_i_max

    if (results[1::7].count(1) + results[2::7].count(1)) > (results[1::7].count(0) + results[2::7].count(0)):
        s_n_max = results[1::7].count(1) + results[2::7].count(1)
        personality_type += "S"
    else:
        s_n_max = results[1::7].count(0) + results[2::7].count(0)
        personality_type += "N"

    sn = s_n_max

    if (results[3::7].count(1) + results[4::7].count(1)) > (results[3::7].count(0) + results[4::7].count(0)):
        t_f_max = results[3::7].count(1) + results[4::7].count(1)
        personality_type += "T"
    else:
        t_f_max =  results[3::7].count(0) + results[4::7].count(0)
        personality_type += "F"

    tf = t_f_max

    if (results[5::7].count(1) + results[6::7].count(1)) > (results[5::7].count(0) + results[6::7].count(0)):
        j_p_max = results[5::7].count(1) + results[6::7].count(1)
        personality_type += "J"
    else:
        j_p_max = results[5::7].count(0) + results[6::7].count(0)
        personality_type += "P"

    jp = j_p_max

    return [[personality_type, ei + sn + tf + jp], [ei, sn, tf, jp]]

