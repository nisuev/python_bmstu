#Вводится текст текст разделяется на предложения по .!?
#Найти предложения в которых четное кол-во слов, слова - только на кириллице
def crit(word):
    kir = 'йцукенгшщзхъфывапролджэячсмитьбю'
    word = word.lower()
    if word.isalpha():
        for i in word:
            if i not in kir:
                return 0
        else:
            return 1
    else:
        return 0

text = ["Мы стоим в девяти километрах от фронта. Вчера сменили, и теперь, набив желудок белыми бобами с",
        "говядиной, все сыты и довольны? Каждый 10+2 сумел даже запастись на вечер полным котелком и вдобавок получить",
        "двойной паек колбасы и хлеба, а это уже кое-что. Давненько такого не бывало: красномордый кашевар",
        "предлагает жратву; каждого, кто проходит мимо, подзывает 11-3 взмахом черпака и накладывает щедрую порцию. Он",
        "в полном отчаянии, потому что знать не знает, как бы 4+5-1 опорожнить походную кухню. Тьяден и Мюллер",
        "раздобыли несколько умывальных тазиков, и он наполнил их вровень с краями, про запас! Тьяден поступает",
        "так от ненасытности, Мюллер – из осторожности. Куда у Тьядена. все это девается, для всех загадка. Он был",
        "и остается тощим как 2+1-12 селедка."]

symb = ''
for i in range(len(text)):
    symb += '.' * text[i].count('.')
    if text[i].count('!') != 0:
        symb += '!' * text[i].count('!')
        text[i] = text[i].replace('!','.')
    if text[i].count('?') != 0:
        symb += '?' * text[i].count('?')
        text[i] = text[i].replace('?','.')

text_str = ''
for i in range(len(text)):
    text_str += text[i]

sent = text_str.split('.')
sent.pop(-1)
for i in range(len(sent)):
    sent[i] += symb[i]

n_sen = sent.copy()
symb = '.:;!?,'
sen_ind = []
for i in range(len(n_sen)):
    for j in symb:
        if j in n_sen[i]:
            n_sen[i] = n_sen[i].replace(j,'')

    if ' - ' in n_sen[i]:
        n_sen[i] = n_sen[i].replace(' - ',' ')

    words = n_sen[i].split()
    crit_cur = 0
    for l in words:
        if crit(l) != 0:
            crit_cur += 1
        else:
            crit_cur = 0
            break

    if crit_cur != 0:
        if crit_cur % 2 == 0:

            sen_ind.append(i)

for i in sen_ind:
    print(sent[i].strip())



