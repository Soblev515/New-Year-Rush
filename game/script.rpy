define b = Character('Генадий Петрович', color="#778899", image="boss")
define g = Character('Колян', color="#006400")
define t = Character('Иван Васильевич', color="#FFE4C4")
define t1 = Character('Ванек', color="#FFE4C4")
define n = Character('Девушка', color="#4B0082", image="Nika")
define n1 = Character('Ника', color="#4B0082", image="Nika")

define book = Character(what_italic = True, kind = nvl)

#Тренинг или книги
define training = False
#Знакомство с Никай
define goodAcquaintance = False
#Спрашивал ли про парня
define boyfriend = False

init:
    $bp = Position(xalign=0.7)

    #Счетчик диалога c Никай на тренинге
    $sympathy = 0

label start:
    label Day_1:

        scene black
        show text "{size=50}День 1{/size}" at truecenter
        with Dissolve(2)
        pause 3

        scene workplace with Dissolve(2)
        hide text

        "{cps=30}Ещё один рабочий день.{w}
        Как же я уже устал от этого.{w}
        Надеюсь, сегодня всё пройдет гладко, и я смогу увильнуть от любой работы.{w}
        Но этому не суждено было сбыться.{w}
        Ведь начальник уже заметил меня и вызвал к себе.{/cps}"

        "{cps=30}Это не к добру.{/cps}"

        "{cps=30}Ещё никогда не было случая, когда люди выходили из его кабинета счастливые и с улыбкой на лице.{w}
        Скорее всего у меня это тоже не получится.{/cps}"

        "{cps=30}Надо идти.{/cps}"

        "{cps=30}Пролетая мимо своих коллег, я быстро дошёл до кабинета начальника.{w}
        Чем раньше это закончится, тем лучше.{/cps}"

        "{cps=30}Вот я стою у двери.{w}
        Я бы сказал, что страх заставил меня остановиться, а сердце бьётся куда быстрее обычного, но это была бы наглая ложь.{/cps}"

        "{cps=30}Для человека, который бывал в этом кабинете уже раза 4 за последний месяц, ещё один такой не страшен.{/cps}"

        "{cps=30}Всё пойдёт по одному и тому же сценарию.{w}
        Я зайду{w}, мы поздороваемся{w}, я сяду{w}, он выскажет, что недоволен мной и заставит написать какую-нибудь статью{w}, иначе уволит.{/cps}"

        "{cps=30}Как же всё предсказуемо.{/cps}"

        "{cps=30}В любом случае, нужно пережить этот сценарий ещё раз.{/cps}"

        menu:
            "Стоит ли мне постучать?"

            "Да":
                "{cps=30}Постучав в дверь два раза, я услышал громкое и чёткое:{w}«Входите!»{/cps}"
            "Нет":
                "{cps=30}А собственно, зачем стучать.{w} Он меня вызвал, значит ожидает того, что я могу войти в любой момент.{/cps}"

        scene bossoffice with fade
        show boss at bp with dissolve

        "{cps=30}Открыв дверь и войдя в кабинет, меня пригласили сесть за стол.{w}
        Что ж.{w}
        Начнём ещё одну цепочку событий, с заранее известным концом.{/cps}"

        b"{cps=30}Ты догадываешься, зачем я тебя позвал?{/cps}"

        g"{cps=30}Нет.{w}
        Я точно знаю.{w}
        Статью на какую тему мне в этот раз написать?{/cps}"

        b"{cps=30}То, что придётся писать, ты понял правильно.{w}
        Но не статью, это слишком легко для тебя.{w}
        В этот раз ты будешь вести целую колонку.{w}
        Про этикет.{/cps}"

        "{cps=30}Что-то новенькое.{w}
        Неужели моя интуиция меня подвела.{w}
        И зачем мне писать колонку про этикет?{w}
        Почему именно про этикет?{w}
        Нормальные темы кончились?{w}
        В любом случае, если я хочу остаться здесь, надо писать.{/cps}"

        g"{cps=30}Понял.{w}
        Уверен, что я смогу справиться с вашим поручением.{w}
        Разрешите откланяться?{/cps}"

        b"{cps=30}Разрешаю.{w}
        И помни, что, если не напишешь, уволю.{/cps}"

        g"{cps=30}Помню.{/cps}"

        scene workplace with fade
        hide boss with dissolve

        "{cps=30}Сказав последние слова, я вышел из кабинета и закрыл дверь.{/cps}"

        "{cps=30}Что ж.{w}
        Если статью я мог написать, и потом валять дурака долгое время, то тут мне нужно будет периодически писать на не интересную мне тему, и всё это под пристальным наблюдением начальника.{/cps}"

        "{cps=30}Вот это подстава.{w}
        Как же крупно я влип.{w}
        Но ничего не поделаешь.{w}
        Надо писать.{w}
        После чашечки кофе обязательно начну.{/cps}"

        "{cps=30}Подойдя к кофейному автомату, я решил, что латте лучше всего подойдёт для того, чтобы начать работать.{/cps}"

        "{cps=30}Подождав, когда латте будет готово, я забрал его и устремился к своему рабочему месту.{w}
        Но придя к нему я понял, что рабочий день уже закончен.{/cps}"

        "{cps=30}Что ж.{w}
        Не в этот раз, этикет, не в этот раз.{w}
        Как же приятно избавиться от работы, не начав её.{w}
        Раз так получилось, пойду домой.{w}
        А завтра навалюсь с новой силой.{/cps}"

        "{cps=30}Собрав свои вещи в рюкзак, я поспешил выйти из этого порядком надоевшего мне здания.{/cps}"

        "{cps=30}Как же хочется побыстрее оказаться дома.{/cps}"

        "{cps=30}Буду лежать на кровати, слушать музыку и представлять себе свободную от написания неинтересных статей и колонок жизнь.{w}
        Как же это прекрасно!{/cps}"

        "{cps=30}Но это будет дома.{w}
        А до него ещё нужно добраться.{w}
        Так что пойду-ка я к остановке.{/cps}"

        scene street2 with fade

        "{cps=30}Выйдя на улицу, я почувствовал всю силу декабрьского мороза.{w}
        Аж вздрогнул.{w}
        Как же холодно.{w}
        Надо скорее дойти домой.{w}
        Я не выдержу пару лишних минут на этом морозе.{/cps}"

        scene busstop2 with fade

        "{cps=30}Дойдя до остановки, я встал в ожидании автобуса.{w}
        Почему же вы так долго едете?{/cps}"

        "{cps=30}Вечер, холодные и голодные люди хотят домой.{w}
        Имейте уважение.{w}
        Но тут к остановке приблизился автобус.{w}
        Мои молитвы были услышаны.{/cps}"

        scene busstop2 with fade

        "{cps=30}Зайдя в него, я сел у окна и стал пристально в него всматриваться.{w}
        Как-будто хотел запомнить всё, что происходит на улице.{w}
        Ну или просто выпитое латте не давало мне уснуть, поэтому я искал себе занятие.{/cps}"

        "{cps=30}На улице шёл снег, люди спешили по своим делам, но скорее всего они шли домой.{/cps}"

        "{cps=30}В автобусе играло радио, но я почти не слушал его.{w}
        Пытался сконцентрироваться на своих  глупых мыслях о своей жизни, и выпасть из реальности на время поездки.{w}
        Хотя ехать мне всего пару остановок.{/cps}"

        scene nightroom with fade

        "{cps=30}Как же хорошо вновь оказаться дома.{/cps}"

        "{cps=30}Уютная постель, вечно включённый экран компьютера.{w}
        Музыка, играющая из наушников на полную громкость.{w}
        И немножко вредной пищи, которую доставляют курьеры.{/cps}"

        "{cps=30}Это Рай на земле.{/cps}"

        "{cps=30}Лучшее, что могло придумать человечество.{w}
        Так бы и не покидал это место никогда.{w}
        Но надо работать.{/cps}"

        "{cps=30}Почему я не могу работать из дома?{w}
        У меня для этого созданы все условия.{w}
        Какая разница, где я буду писать статьи, здесь или в офисе.{w}
        Их качество же от этого не зависит.{/cps}"

        "{cps=30}Проведя ещё один бессмысленный вечер своей жизни за залипанием в соцсетях, я решил, что пора бы уже ложиться спать.{/cps}"

        "{cps=30}Завтра опять идти на работу и писать какую-то дурацкую колонку.{w}
        Если смогу закончить работу утром, то весь день можно будет ничего не делать.{w}
        Такая перспектива меня привлекает.{/cps}"

        "{cps=30}Ладно.{/cps}"

        "{cps=30}Чем меньше мыслей перед сном, тем быстрее он приходит.{/cps}"

        "{cps=30}Морфей, я иду к тебе.{/cps}"

        jump Day_2

    label Day_2:

        scene room
        with Dissolve(5)

        scene black
        show text "{size=50}День 2{/size}" at truecenter
        with Dissolve(2)
        pause 3

        scene room with Dissolve(2)
        hide text

        "{cps=30}Я слышу зов.{w}
        Но не из глубин морей и океанов, а из-под моей подушки.{/cps}"

        "{cps=30}Будильник, который заведён на телефоне с самого первого рабочего дня, и не выключающийся всё это время, пробудил меня.{/cps}"

        "{cps=30}Ещё один рабочий день.{w}
        Какая же это морока.{w}
        Хотя, меня никто не спрашивает.{w}
        Хочешь жить, умей работать.{/cps}"

        "{cps=30}Говорится вроде немного не так, но именно эта фраза описывает всю суть современной жизни.{w}
        Пора собираться на эту самую работу, что позволяет мне жить.{/cps}"

        "{cps=30}Завершив все свои утренние дела, такие как умывание и небольшой завтрак, состоящий из чашечки кофе и пары бутербродов, я оделся и отправился на работу.{/cps}"

        scene street3 with fade

        "{cps=30}Этим утром было куда теплее, нежели предыдущим.{w}
        По крайней мере у меня не появилось идеи вернуться обратно в кровать, и не выходить никуда.{/cps}"

        "{cps=30}А может на это повлияло горячее кофе?{w}
        Кто знает?{w}
        Сейчас главное не это, а то, как быстро я смогу добраться до своего рабочего места, и как быстро смогу его покинуть.{/cps}"

        "{cps=30}Благо, остановка не далеко от моего дома.{w}
        Надеюсь, автобус приедет быстро и мне не придётся его ждать.{w}
        Хоть сегодня и теплее, но всё ещё холодно.{/cps}"

        "{cps=30}Прождав около двух минут, я увидел приближающийся автобус и поспешил занять место.{w}
        Хотя смысла в этом не было, ведь на остановке кроме меня никого не было, собственно, как и в автобусе.{/cps}"

        scene workplace with fade

        "{cps=30}И снова знакомое офисное здание, рабочий стол, коллеги, которые неизвестно откуда взялись.{w}
        Может, они здесь ночуют?{/cps}"

        "{cps=30}Хотя, меня это волновать не должно. Нужно сделать работу.{w}
        А самый быстрый способ её завершить - это обратиться к Википедии.{w}
        Относительно надёжный источник любой информации.{/cps}"

        "{cps=30}Сколько раз она меня спасала за всю мою жизнь, я уже и не помню.{w}
        Может, поможет и в этот раз.{/cps}"

        "{cps=30}Так-с, мне нужно написать про этикет.{w}
        О, Всемогущий источник знаний, расскажи мне, что такое этикет.{/cps}"

        book'''
        {cps=30}Этикет (от фр. étiquette — этикетка, надпись) — правила поведения людей в обществе, поддерживающие представления данного общества о подобающем.{/cps}

        {cps=30}В современном виде и значении слово было впервые употреблено при дворе короля Франции Людовика XIV — гостям были розданы карточки (этикетки) с изложением того,{/cps}

        {cps=30}как они должны держаться; хотя определённые своды норм и правил поведения существовали уже с древнейших времён.{/cps}'''
        nvl clear
        nvl hide

        "{cps=30}Ну что ж.{w}
        Вот и готово.{/cps}"

        "{cps=30}Даже не знаю, как из этого можно вынести информации на целую колонку.{w}
        Думаю, одной небольшой статьи ему должно хватить.{w}
        Сейчас немного отредактируем, поправим шрифт и всё будет готово.{/cps}"

        "{cps=30}После небольшой работы над визуальной составляющей текста, я решил, что работу можно сдать.{w}
        Быстро же я сегодня управился.{/cps}"

        "{cps=30}Пора идти к начальнику.{w}
        С этими мыслями и лицом победителя я отправился со своей работой к кабинету начальника.{/cps}"

        "{cps=30}Предварительно постучав, чтобы сообщить о своём присутствии, я зашёл в кабинет.{/cps}"

        scene bossoffice with fade
        show boss at bp with dissolve

        g"{cps=30}Доброе утро.{w}
        Вот готовая статья про этикет.{w}
        И не нужно вести целую колонку.{/cps}"

        "{cps=30}Начальник быстро просмотрел мою статью.{/cps}"

        b"{cps=30}Это, конечно хорошо, но это не то.{w}
        Лучше возьми книги по этикету, почитай их, и уже тогда приходи с готовой колонкой.{w}
        Может сам узнаешь что-нибудь новое.{w}
        Понял?{/cps}"

        "{cps=30}Бам, и со счётом 1:0 я улетел в нокаут.{w}
        Читать книжки?{w}
        Чтобы вести колонку?{w}
        Что это за ересь?{/cps}"

        "{cps=30}Ещё множество подобных вопросов возникло в моей голове.{w}
        Но с начальником спорить - себе дороже.{w}
        Так что лучше мне всё-таки переделать это.{/cps}"

        g"{cps=30}Понял, переделаю.{/cps}"

        b"{cps=30}Уж постарайся.{/cps}"

        "{cps=30}После этих слов я вышел из кабинета начальника и закрыл за собой дверь.{/cps}"

        scene workplace with fade
        hide boss with dissolve

        "{cps=30}Опять из-за своей глупости я увеличил количество своей работы.{w}
        Может и правда стоит читать книжки?{/cps}"

        "{cps=30}Но не просто свод правил этикета, а про эффективность людей, развитие мышления и прочее.{w}
        Где же мне раздобыть такую ценную литературу?{/cps}"

        "{cps=30}Вроде как на пару этажей ниже нашего офиса находится какая-то библиотека.{w}
        Хотя, может быть существуют какие-то мастер классы или тренинги этикета, а то читать как-то лень.{/cps}"

        "{cps=30}Я могу либо пойти посмотреть библиотеку, либо поискать в интернете что-нибудь про тренинги.{/cps}"

        menu:
            "Пойти на тренинги":
                $training = True
            "Сходить в библиотеку":
                $training = False

        if training:
            "{cps=30}Лень 1, чтение книг 0.{w}
            Хотя это все субъективно, сейчас мне нужно найти того, кто сможет рассказать мне про этот этикет.{/cps}"

            "{cps=30}Так...{/cps}"

            "{cps=30}Вроде нашёл.{w}
            Бесплатные тренинги “Как общаться в современном обществе”.{w}
            Сегодня вечером.{w}
            Хм, наверное стоит наведаться, в любом случае если не понравится могу просто уйти, бесплатно же.{/cps}"

            scene trainingroom with fade

            "{cps=30}В комнате находится человек 7, и они выглядят{w}…{w} обычно.{/cps}"

            "{cps=30}Такие же серые мыши как и я.{w}
            Мы садимся на подготовленные для нас места и через время перед нами появляется человек лет 35, высокий и стройный.{/cps}"

            show colleague3 with dissolve

            t"{cps=30}Всем добрый вечер, меня зовут Дмитриенко Иван Васильевич и я являюсь специалистом по этикету.{/cps}"

            "{cps=30}Дмитриенко Иван Васильевич, как официально.{w}
            Как бы сократить?{w}
            Хм{w}, придумал{w} - будешь Ваньком!{/cps}"

            t1"{cps=30}Я преподаю этикет и этику, как науку в университете.{w}
            Но здесь мы не будем так сильно углубляться в нее и будем рассматривать этикет как инструмент, или даже я бы сказал, необходимый инструмент в современном обществе.{/cps}"

            "{cps=30}А я обычно стараюсь отстраниться от этого.{/cps}"

            t1"{cps=30}Общение осуществляется с помощью диалога, цель которого – установление понимания между людьми.{w}
            {b}Задача общения – установление взаимопонимания.{/b}{/cps}"

            t1"{cps=30}В связи с этим культура общения превращается в систему норм, принципов и правил.{/cps}"

            t1"{cps=30}Она предполагает знание, понимание и соблюдение основных норм межличностного общения, включающих совокупные действия многих факторов: нравственных{w}, психологических{w}, социокультурных{w}, «технологических».{/cps}"

            t1"{cps=30}Именно эти факторы мы и будем с вами тренировать.{w}
            Почему бы нам не начать с простого диалога, поделитесь на пары и расскажите о себе.{/cps}"

            "{cps=30}Простой диалог?{w}
            Типо: “Привет, меня зовут Колян, а как тебя?”, “Угу очень захватывающая история.”{/cps}"

            "{cps=30}Не вижу проблем{w}...{w} кроме того что нужно общаться с кем-то.{/cps}"

            show colleague3 at right with move
            show Nika with dissolve

            "{cps=30}Ко мне подходит девушка лет 20.{w}
            Она пристально, но скромно смотрит на меня.{w}
            Как хищник на своей первой охоте.{w}
            Видимо она хочет, чтобы мы были в паре?{/cps}"

            show Nika at left with move

            menu:
                "Предложить быть в паре":
                    g"{cps=30}Эй, не хочешь объединиться?{/cps}"

                    "{cps=30}Она удивленно смотрит на меня, при этом в её глазах можно было заметить и радость.{/cps}"

                    "{cps=30}Она добилась своей цели, поймала меня в свою ловушку.{w}
                    Но продолжает играть в тихую и невинную девушку.{/cps}"

                    n"{cps=30}Да.{/cps}"

                    "{cps=30}Вот и всё.{w}
                    Теперь я в её плену.{w}
                    Причём ещё и по собственной воле.{/cps}"

                    "{cps=30}Но если уж я взялся за это дело, то доведу его до конца.{/cps}"

                "Игнорировать":
                    "{cps=30}Я посмотрел в противоположную сторону от нее, как бы ища себе партнера.{w}
                    Но заметил, что все уже распределились и мы остались вдвоем.{/cps}"

                    "{cps=30}Если судьба, бог или другие высшие силы хотят этого, то пусть так оно и будет.{/cps}"

            t1"{cps=30}Друзья!{/cps}"

            "{cps=30}Заговорил подошедший к нам Ванек.{/cps}"

            t1"{cps=30}Не стесняйтесь!{w}
            Я знаю, что начать общаться с незнакомым человеком сложно, но попытайтесь представить, что это квест, в котором вам нужно узнать как можно больше о собеседнике!{/cps}"

            "{cps=30}Квест?{w}
            Мы что в игре какой-то?{/cps}"

            hide colleague3 with dissolve
            show Nika at center with move

            "{cps=30}Мы сели напротив друг друга.{w}
            Она с интересом смотрела на меня.{w}
            Думаю мне стоит первым начать наш диалог.{w}
            Кто знает, что у неё сейчас в голове вертится?{/cps}"

            default menuset = set()
            menu m:
                set menuset
                "Рассказать о себе":
                    $sympathy += 1

                    g"{cps=30}Привет.{w}
                    Меня зовут Николай, можно просто Колян.{w}
                    Я работаю журналистом.{w}
                    Мне поручили вести колонку про этикет, поэтому я сюда и пришёл.{w}
                    А как тебя зовут?{/cps}"


                "Расспросить её":
                    $sympathy -= 1

                    g"{cps=30}Меня зовут Николай.{w}
                    Я в таких местах в первый раз, поэтому позволю тебе начать первой.{/cps}"

                "Поговорить о погоде":
                    g"{cps=30}Холодная зима в этом году, ну, по сравнению с предыдущими.{/cps}"

                    n"{cps=30}Да.{/cps}"

                    "{cps=30}в её голосе слышалась нотка отчаяния.{w}
                    Видимо, я иду не по её плану.{w}
                    Надо попытаться узнать как её зовут.{/cps}"

                    jump m

            n1"{cps=30}Меня зовут Ника.{w}
            Я учусь на юриста.{w}
            Сюда пришла, чтобы отвлечься от  учёбы и пообщаться хоть с кем-то кроме преподавателей и библиотекарей.{/cps}"

            "{cps=30}Как же это знакомо.{/cps}"

            "{cps=30} Сам был такой, когда учился.{w}
            Думаю, общаться будет легко.{w}
            Особенно, зная её истинные намерения.{/cps}"

            "{cps=30}Или это очередная игра?{w}
            Какие же люди всё-таки сложные существа.{/cps}"

            menu m1:
                set menuset
                "Узнать о её успехах в учебе":
                    n1"{cps=30}Ну я очень усердно учусь, поэтому учёба проблем не доставляет.{/cps}"

                    menu:
                        "Похвалить":
                            $sympathy += 1

                            g"{cps=30}Ты молодец, наверное твои родные гордятся тобой.{/cps}"

                            n1"{cps=30}Да, так оно и есть.{/cps}"

                        "Промолчать":
                            "{cps=30}Если буду молчать, то такими темпами вообще ничего не добьюсь.{w}
                            Нужно хоть что-то сказать.{/cps}"
                    jump m1

                "Узнать о её друзьях":
                    n1"{cps=30}У меня мало друзей, поэтому и говорить не о ком. Почти всё время трачу на учёбу.{/cps}"

                    jump m1

                "Узнать, есть ли у неё парень":
                    $sympathy -= 1
                    $boyfriend = True

                    n1"{cps=30}Не думаю, что это подходящий вопрос для девушки при первом знакомстве, не находишь?{/cps}"

                    "{cps=30}Как я сразу об этом не подумал.{w}
                    Видимо мои навыки общения с людьми действительно атрофировались за столько лет.{/cps}"

                    "{cps=30}Я уже хотел сменить тему разговора, как услышал...{/cps}"

                    n1"{cps=30}Нет, я свободна.{/cps}"

                    "{cps=30}Сказав это она странно улыбнулась, но я не обратил на это внимания.{/cps}"

                    jump m1

                "Промолчать":
                    "{cps=30}На этом наш не очень конструктивный диалог закончился, так как никто из нас не знал, как его продолжить.{/cps}"

            if boyfriend:
                "{cps=30}Видимо, мне всё-таки стоит больше учиться общаться с людьми.{w}
                И не задавать лишних вопросов.{w}
                Хотя бы так рано.{/cps}"

            show colleague3 at right with dissolve

            t1"{cps=30}Ну вот и все, на этом наше занятие закончилось.{w}
            Я знаю что вам было тяжело, потому что создавать новые отношения общения это сложно.{/cps}"

            t1"{cps=30}И на следующем занятии, мы поговорим, как можно упростить этот этап.{w}
            Встречаемся завтра, всем пока.{/cps}"

            hide colleague3 at right with move
            show Nika at center with move

            if sympathy == 2:
                $goodAcquaintance = True
                n1"{cps=30}Спасибо за беседу, мне пора.{w}..{w}увидимся.{/cps}"

                "{cps=30}Я увидел, что она была рада пообщаться со мной, потому что на её лице появилась улыбка.{/cps}"

                g"{cps=30}Прощай, до скорого.{/cps}"

            if sympathy == -2:
                "{cps=30}Ника собрала свои вещи и ушла.{/cps}"

            else:
                n1"{cps=30}Думаю, на этом всё.{w}
                Ещё увидимся.{/cps}"

                g"{cps=30}Пока.{/cps}"


        else:
            "{cps=30}Может действительно сходить в библиотеку?{w}
            Вроде у нас недалеко от офиса была одна.{/cps}"

            "{cps=30}Не знаю, конечно, есть ли там хоть что-то про этикет.{w}
            Есть ли вообще хоть где-нибудь.{w}
            Удачу попытать всё равно стоит.{/cps}"

            "{cps=30}Я могу быть глупым, скучным, но удача всегда была со мной.{w}
            Вот и сейчас буду надеяться на неё.{w}
            Вперёд, в библиотеку.{w}
            На поиски знаний.{/cps}"

            scene library with fade

            "{cps=30}Спустя некоторое время я уже стоял в библиотеке с книгами в руках.{w}
            Тут должно быть то, что мне нужно.{w}
            Главное это найти.{/cps}"

            "{cps=30}Самое ужасное в этой ситуации, что мне недоступны столь мощные инструменты современного мира, такие как Ctrl+C и Ctrl+V.{w}
            Вместе с ними я бы справился с этой работой куда быстрее.{w}
            Но раз их у меня нет, придётся читать.{/cps}"

            book'''
            {cps=30}{i}{b}Культура поведения{/b} – составная часть культуры человека, она выступает внешним выражением духовного богатства индивида, его внутреннего мира.{/i}{/cps}

            {cps=30}{i}Это совокупность форм повседневного поведения человека (в труде, быту, общении), в них проявляется внешнее выражение нравственных и эстетических норм его поведения.{/i}{/cps}

            {cps=30}{i}В широком смысле понятие «культура поведения» объединяет все стороны внешней культуры человека:{/i}{/cps}

            {cps=30}{i}этикет, правила общения и поведения в общественных местах, культуру быта, которая предполагает включение личных потребностей и интересов,{/i}{/cps}

            {cps=30}{i}взаимоотношения с людьми вне работы. Внешняя культура человека наглядна, ее сразу же можно оценить по тому, как человек говорит, как держит себя с окружающими, как одевается.{/i}{/cps}

            {cps=30}{i}И именно на основе внешней культуры складывается о нас внешнее впечатление.{/i}{/cps}'''

            nvl clear

            book'''
            {cps=30}{i}Но во внешней культуре проявляется и внутренняя культура личности.{/i}{/cps}

            {cps=30}{i}Важны не форма общения и поведения сами по себе, а их мотивы, внутренняя воспитанность, которая обуславливает поведение людей.{/i}{/cps}

            {cps=30}{i}Воспитанный человек вежлив и учтив не потому, что хочет красиво выглядеть, а потому, что уважение к людям, внимание к ним, душевный такт не позволяют ему быть другим.{/i}{/cps}'''
            nvl clear
            nvl hide

            "{cps=30}Хм...{w} А книги оказывается не так уж и плохи.{w}
            Можно узнать действительно много интересного.{/cps}"

            "{cps=30}Думаю, стоит взять их на время.{w}
            Пока буду вести колонку они ещё не раз меня выручат.{/cps}"

            "{cps=30}Подойдя к стойке с библиотекарем, я дал ему знать, что книги мной были взяты и верну их через некоторое время.{w}
            Он что-то отметил в компьютере и отпустил меня.{w}
            Отлично.{/cps}"

        scene black with fade

        "{cps=30}После огромного количества времени, потраченного на понимание этикета, я очень устал.{/cps}"

        "{cps=30}Так что теперь мне нужен отдых, желательно дома, на кровати, с вкусной вредной едой и вредными напитками.{w}
        Хотя как можно назвать вредным то, что приносит такое удовольствие.{/cps}"

        "{cps=30}И вот опять я мечтаю поскорее оказаться дома, как и вчера, и позавчера, и каждый свой рабочий день.{/cps}"

        "{cps=30}А почему?{w}
        Дома я ничего не делаю, прожигаю “лучшие” годы своей жизни непонятно на что.{/cps}"

        "{cps=30}И тем не менее, я ни разу не задумывался об этом до сегодняшнего дня.{w}
        Почему именно сегодня меня озарили такие мысли?{w}
        Почему именно такие мысли посетили мою голову в принципе?{/cps}"

        "{cps=30}Кажется, мне нужно что-то, что будет меня отвлекать от столь пессимистичных вещей.{w}
        Найти себе хобби, больше общаться с людьми, завести больше друзей.{/cps}"

        "{cps=30}Посмотрим, что из этого выйдет, в любом случае я могу вернуться в свое привычное состояние.{/cps}"

        scene street6 with fade

        "{cps=30}Пока я размышлял обо всём этом, я быстро собрался и покинул офисное здание.{/cps}"

        "{cps=30}Находиться здесь большее количество времени я не желал, да и смысла в этом особого не было.{w}
        Все равно ничего не делаю.{/cps}"

        "{cps=30}На улице была всё ещё хорошая погода.{w}
        Не очень холодно, без ветра, без осадков.{w}
        Просто прекрасно.{/cps}"

        "{cps=30}Хоть что-то меня радует в сегодняшнем дне.{w}
        Думаю, ради этого  можно даже прогуляться, все равно идти не очень далеко.{/cps}"

        scene street2 with fade

        "{cps=30}Пройтись до дома было хорошей идеей.{/cps}"

        "{cps=30}Я очистился от мрачных мыслей, подышал свежим воздухом.{w}
        Вокруг меня проходит множество людей.{w}
        У них у всех свои мысли, свои проблемы, своя жизнь.{/cps}"

        "{cps=30}И моя жизнь ничем не отличается от их.{w}
        Но при этом каждая жизнь уникальна по своему.{w}
        Как же это парадоксально.{/cps}"

        scene nightroom with fade

        "{cps=30}Дойдя с такими мыслями до дома, я зашел в квартиру и решил, что лучше всего сейчас будет просто поспать.{/cps}"

        "{cps=30}Сон - лучшее лекарство.{/cps}"

        jump Day_3

    label Day_3:

        scene black
        show text "{size=50}День 3{/size}" at truecenter
        with Dissolve(2)
        pause 3

        scene room with Dissolve(2)

        "{cps=30}Новый день - новые знания.{/cps}"

        jump Day_4

    label Day_4:



        jump Day_5

    label Day_5:



        jump Day_6

    label Day_6:



        jump Day_7

    label Day_7:



        return

    # "{cps=30}{/cps}"
