from django.db                      import models
from django.contrib.auth.models     import AbstractBaseUser, PermissionsMixin, BaseUserManager 
from django.contrib.auth.hashers    import make_password #Make_password recibe el password original, lo envía al hasher y devuelve una contraseña encriptada a través de una palabra clave


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
    # Crear y guardar usuarios que debe ingresar con username y password
        if not username:
            raise ValueError('El campo de usuario no puede estar vacío')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, username_, password_):
    # Crear y guardar superusuarios o administradores con nombre de usuario y contraseña.
        user = self.create_user(
            username=username_,
            password=password_,
        )
        user.is_admin = True #Define el usuario como administrador
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id      = models.IntegerField(primary_key=True)
    username    = models.CharField('Username', max_length = 45, unique=True)
    password    = models.CharField('Password', max_length = 256)
    name        = models.CharField('Name', max_length = 45)
    lastname    = models.CharField('lastname', max_length= 45)
    email       = models.EmailField('Email', max_length = 100)
    
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    
    objects = UserManager()
    USERNAME_FIELD = 'username'