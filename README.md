# web

<h5>Список правок:</h5>
1) (ок) Убрать медиа из репозитория, UGC контент должен быть только на серверах, настроить .гитигнор, у тебя питонячий кеш в репах.
2) (ок) user = models.ForeignKey(Creator, on_delete=models.SET_NULL, null=True) разве лайк может быть без хозяина? Он же не ронин.
3) (доделать) Если я буду заливать вместо png (file = models.ImageField(verbose_name='File') ), большой файл, например txt, как ты будешь с этим бороться? 
4) (доделать) Если напишешь 2-3 теста на каждый модуль будет очень круто, для понимания этого момента.
5) (доделать) Давай сделаем проверку тегов на уникальность на уровне базы.
6) (доделать) Почему локация в чарфилде?
7) (доделать) Почему user = models.OneToOneField(User, on_delete=models.CASCADE) делай через абстрактоного юзера
8) (ок) Не хардкодь! MEDIA_ROOT = u'/home/anton1202/MyOwnInstagram/media' MEDIA_URL = '/media/' STATIC_ROOT = u'/home/anton1202/MyOwnInstagram/static' STATIC_URL = '/static/‘ У меня это работать не будет, и на прод серверах! Плохо!
9) (не уверен!) Уверен? @authentication_classes([OAuth2Authentication, SocialAuthentication, CsrfE