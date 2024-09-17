    #Характеристики в самом низу для того, чтобы они были над фрагментом при непосредственном его воспроизведении
    print('----------------------------------------')
    print('')
    print('Характеристики: ')
    print('')
    print('Здоровье:', H_H, '(', max_H_H, ')')
    print('')
    print('Мастерство:', A_H, '(', max_A_H, ')')
    print('')
    print('Удача:', L_H, '(', max_L_H, ')')
    print('')
    print('Деньги:', M_H)
    print('')
    print('Еда:', F_H)
    print('')
    print('Инвентарь:', len(inv_list),'/',max_inv)
    print('')
    print(inv_list)
    print('')
    if left_hand == 1:
        print('В левой руке: ',left_hand_ls)
        print('')
    print('----------------------------------------')
    print('')
    if F_H > 0:
        print('')
        F_CH = int(input('Если вы хотите поесть, нажмите 1, если не хотите, нажмите 0: '))
        print('')
    while F_CH == 1 and F_H > 0:
        H_H = H_H + 3
        if H_H > max_H_H:
            H_H = max_H_H
        print('')
        print('Вы поели! Ваша выносливость - ',H_H)
        print('')
        F_CH = int(input('Если хотите поесть еще, нажмите 1, если не хотите, нажмите 0: '))
        print('')
        print('----------------------------------------')
    if F_CH == 1 and F_H <= 0:
        print('У вас нет еды.')
        print('')
        print('----------------------------------------')


#Добавление новых вещей
    print('')
    inv_add = int(input('Если вы хотите подобрать новую вещь, нажмите 1, если вы не желаете ее подбирать, нажмите 0: '))
    print('')

    if inv_add == 1 and len(inv_list) >= max_inv:
        print('')
        print('Вам не хватает места, чтобы взять новую вещь.')
        print('')
        inv_rem = int(input('Если вы хотите выбросить вещь, нажмите 1, если вы хотите оставить вещь, нажмите 0: '))
        print('')
        if inv_rem == 1:
            print(inv_list)
            print('')
            inv_rem_ch = int(input('Введите номер вещи, которую желаете выбросить: '))
            print('')
            inv_rem_ch = inv_rem_ch - 1
            inv_list.pop(inv_rem_ch)
            print('Вы выбросили предмет.')
            print('')

    if inv_add == 1 and len(inv_list) < max_inv:
        print('Вы подобрали новый предмет.')
        print('')
        inv_list.append('Сама вещь.')
        print('')

#Выбрасывние вещей
    print('')
    inv_rem = int(input('Если вы хотите выбросить вещь, нажмите 1, если вы хотите оставить вещь, нажмите 0: '))
    print('')
    if inv_rem == 1:
        print(inv_list)
        print('')
        inv_rem_ch = int(input('Введите номер вещи, которую желаете выбросить: '))
        inv_rem_ch = inv_rem_ch - 1
        inv_list.pop(inv_rem_ch)

#Заполнение левой руки
    print('')
    left_hand = int(input('Если хотите взять этот предмет (в левую руку), нажмите 1, если не хотите его брать, нажмите 0: '))
    print('')
    if left_hand == 1 and left_hand_was == 1:#Если в левой руке уже что-то было
        left_hand_ls = 'Предмет'
        print('')
        print('Вы взяли в левую руку предмет - ')
        print('')

    if left_hand == 1 and left_hand_was == 0:#Если в левой руке ничего не было
        left_hand_ls = 'Предмет'
        A_H = A_H - 1
        print('')
        print('Вы взяли в левую руку предмет - ')
        print('')

    if left_hand == 0 and left_hand_was == 1:#Выбрасывание из левой руки
        A_H = A_H + 1
        print('')
        print('Вы выбросили из левой руки предмет - ')
        print('')
