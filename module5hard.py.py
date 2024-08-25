import time
class Video:
    Video = []

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        h = '{title}, {duration}, {time_now}, {adult_mode}.'
        return h.format(self=self, title=self.title, duration=self.duration, time_now=self.time_now,
                        adult_mode=self.adult_mode)
class User:
    User = []

    def __init__(self,
                 nickname,
                 pasword,
                 age):
        self.nickname = nickname
        self.pasword = pasword
        self.age = age
        pasword = hash('pasword')
class UrTube:
    users = []
    videos = []
    current_user = None
    current_user_adult_mode = False

    def __init__(self):
        UrTube.users = []
        UrTube.videos = []

    def register(self, nickname, pasword, age):
        Us = User(nickname, pasword, age)
        if len(UrTube.users) == 0:
            UrTube.users.append(Us)
            UrTube.current_user = nickname
            if age < 18:
                UrTube.current_user_adult_mode = True
        else:
            for i in range(len(UrTube.users)):
                if nickname == UrTube.users[i].nickname:
                    pasword = hash('pasword')
                    if hash(pasword) != hash(UrTube.users[i].pasword):
                        print(f'Пользователь {nickname} уже существует')
                        break
                else:
                    UrTube.current_user = UrTube.users[i].nickname
                    UrTube.users.append(Us)
                    UrTube.current_user = nickname
                    if age < 18:
                        UrTube.current_user_adult_mode = True
        return UrTube.current_user

    def add(self, *args):
        for i in range(len(args)):
            if args[i].title in Video.Video:
                pass
            else:
                Video.Video.append(args[i].title)
                UrTube.videos.append(args[i])

    def get_videos(self, word):
        same_words = []
        for i in range(len(UrTube.videos)):
            if word.lower() in UrTube.videos[i].title.lower():
                same_words.append(UrTube.videos[i].title)
        return same_words

    def log_in(self, nickname, pasword):
        for i in range(len(UrTube.users)):
            if nickname == UrTube.users[i].nickname:
                if hash(pasword) == hash(UrTube.users[i].pasword):
                    UrTube.current_user = nickname
                    return UrTube.current_user
                else:
                    print('Неверный пароль')
                    break
            else:
                print('Пользователь не найден')

    def log_out(self):
        current_user = None
        UrTube.current_user_adult_mode = False

    def watch_video(self, args):
        if UrTube.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for i in range(len(UrTube.videos)):
                if args == UrTube.videos[i].title:
                    if UrTube.videos[i].adult_mode == True and UrTube.current_user_adult_mode == True:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                        ur.log_out()
                        break
                    else:
                        for j in range(1, UrTube.videos[i].duration + 1):
                            print(j, end=' ')
                            time.sleep(1)
                        print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')