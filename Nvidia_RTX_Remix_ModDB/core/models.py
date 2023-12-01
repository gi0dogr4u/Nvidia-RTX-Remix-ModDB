from django.db import models


class GraphicAPI(models.Model):
    DIRECTX = 'DIRECTX'
    OPENGL = 'OPENGL'
    VULKAN = 'VULKAN'
    GRAPHICAPI = (
        (DIRECTX, 'DirectX'),
        (OPENGL, 'OpenGL'),
        (VULKAN, 'Vulkan')
    )
    name = models.CharField(max_length=8, choices=GRAPHICAPI)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Graphic Api"
        verbose_name_plural = "Graphic Api's"


class Game(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    release_date = models.DateField()
    graphics_api = models.ForeignKey(GraphicAPI, null=True, blank=True, on_delete=models.SET_NULL)
    poster_image = models.FileField()
    where_to_buy = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Game"
        verbose_name_plural = "Games"


class SuccessLevel(models.Model):
    level = models.IntegerField()
    description = models.CharField(max_length=128)

    def __str__(self):
        return self.level

    class Meta:
        verbose_name = "SuccessLevel"
        verbose_name_plural = "Success Levels"


class DXVKVersion(models.Model):
    tag = models.IntegerField()
    release_date = models.DateField()

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = "DXVK Version"
        verbose_name_plural = "DXVK Versions"


class RemixVersion(models.Model):
    tag = models.CharField(max_length=64)
    release_date = models.DateField()

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = "Remix Version"
        verbose_name_plural = "Remix Versions"


class APIWrapper(models.Model):
    name = models.CharField(max_length=128)
    version = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "API Wrapper"
        verbose_name_plural = "API Wrappers"


class Experiment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    success_level = models.ForeignKey(SuccessLevel, on_delete=models.DO_NOTHING)
    dxvk_version = models.ForeignKey(DXVKVersion, on_delete=models.DO_NOTHING)
    remix_version = models.ForeignKey(RemixVersion, on_delete=models.DO_NOTHING)
    wrappers_used = models.ForeignKey(APIWrapper, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.game

    class Meta:
        verbose_name = "Experiment"
        verbose_name_plural = "Experiments"
