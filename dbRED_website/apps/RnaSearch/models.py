# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
# Create your models here.


class Project_Cellline(models.Model):
    project = models.CharField(max_length = 30, verbose_name=u"project")
    cellline = models.TextField(null=False, verbose_name=u"cellline")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"addtime")
    class Meta:
        verbose_name = u"project's cellline"
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.project


class Human_Rnaedit(models.Model):
    name = models.CharField(max_length=10, verbose_name="Rnaedit_name")
    Chr = models.CharField(max_length=5, verbose_name=u"Chr")
    position = models.IntegerField(default=0, verbose_name=u"position")
    Genename = models.CharField(max_length=200, null=True, blank=True, db_index=True, verbose_name=u"Genename")
    Genedetail = models.TextField(null=True, blank=True, verbose_name='Genedetail')
    Strand = models.CharField(max_length=1, verbose_name='Strand')
    Ref = models.CharField(max_length=1, choices=(('A','A'),('T','T')), verbose_name='Ref')
    Alt = models.CharField(max_length=1, choices=(('G','G'),('C','C')), verbose_name='Alt')
    dbSNP = models.CharField(max_length=20, null=True, verbose_name='dbSNP')
    database = models.CharField(max_length=3, verbose_name='database')
    method = models.CharField(max_length=4, verbose_name='method')
    phastcons = models.FloatField(default=0.0, verbose_name='phastcons')
    Repeat = models.CharField(max_length=6, verbose_name='Repeat')
    Element = models.CharField(max_length=30, verbose_name='Element')
    GeneRegion = models.CharField(max_length=30, verbose_name='GeneRegion')
    AAChange = models.CharField(max_length=20, verbose_name='AAChange')
    Cellline = models.TextField(verbose_name='Cellline')
    Project = models.CharField(max_length=60, verbose_name='Project')
    Sequence = models.CharField(max_length=250, verbose_name=u'Sequence')
    Editlevel = models.FloatField(default=0.0, verbose_name='Editlevel')
    lncRNA = models.TextField(null=True, blank=True, verbose_name='lncRNA')
    circRNA = models.TextField(null=True, blank=True, verbose_name='circRNA')
    miRNA = models.TextField(null=True, blank=True, verbose_name='miRNA')
    piRNA = models.TextField(null=True, blank=True, verbose_name='piRNA')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"addtime")

    class Meta:
        verbose_name = u"Human_Rnaedit"
        verbose_name_plural = verbose_name
        unique_together = ('Chr', 'position',)

    def __unicode__(self):
        return '{0}-{1}'.format(self.name, self.position)


class Mouse_Rnaedit(models.Model):
    name = models.CharField(max_length=10, verbose_name="Rnaedit_name")
    Chr = models.CharField(max_length=5, verbose_name=u"Chr")
    position = models.IntegerField(default=0, verbose_name=u"position")
    Genename = models.CharField(max_length=210, null=True, blank=True, db_index=True, verbose_name=u"Genename")
    Genedetail = models.TextField(null=True, blank=True, verbose_name='Genedetail')
    Strand = models.CharField(max_length=1, verbose_name='Strand')
    Ref = models.CharField(max_length=1, choices=(('A','A'),('T','T')), verbose_name='Ref')
    Alt = models.CharField(max_length=1, choices=(('G','G'),('C','C')), verbose_name='Alt')
    dbSNP = models.CharField(max_length=20, null=True, verbose_name='dbSNP')
    database = models.CharField(max_length=3, verbose_name='database')
    method = models.CharField(max_length=4, verbose_name='method')
    phastcons = models.FloatField(default=0.0, verbose_name='phastcons')
    Repeat = models.CharField(max_length=6, verbose_name='Repeat')
    Element = models.CharField(max_length=30, verbose_name='Element')
    GeneRegion = models.CharField(max_length=30, verbose_name='GeneRegion')
    AAChange = models.CharField(max_length=20, verbose_name='AAChange')
    Cellline = models.TextField(verbose_name='Cellline')
    Sequence = models.CharField(max_length=250, verbose_name=u'Sequence')
    Editlevel = models.FloatField(default=0.0, verbose_name='Editlevel')
    lncRNA = models.TextField(null=True, blank=True, verbose_name='lncRNA')
    circRNA = models.TextField(null=True, blank=True, verbose_name='circRNA')
    miRNA = models.TextField(null=True, blank=True, verbose_name='miRNA')
    piRNA = models.TextField(null=True, blank=True, verbose_name='piRNA')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"addtime")

    class Meta:
        verbose_name = u"Mouse_Rnaedit"
        verbose_name_plural = verbose_name
        unique_together = ('Chr', 'position',)

    def __unicode__(self):
        return '{0}-{1}'.format(self.name, self.position)


class Rat_Rnaedit(models.Model):
    name = models.CharField(max_length=10, verbose_name="Rnaedit_name")
    Chr = models.CharField(max_length=5, verbose_name=u"Chr")
    position = models.IntegerField(default=0, verbose_name=u"position")
    Genename = models.CharField(max_length=200, null=True, blank=True, db_index=True, verbose_name=u"Genename")
    Genedetail = models.TextField(null=True, blank=True, verbose_name='Genedetail')
    Strand = models.CharField(max_length=1, verbose_name='Strand')
    Ref = models.CharField(max_length=1, choices=(('A','A'),('T','T')), verbose_name='Ref')
    Alt = models.CharField(max_length=1, choices=(('G','G'),('C','C')), verbose_name='Alt')
    dbSNP = models.CharField(max_length=20, null=True, verbose_name='dbSNP')
    method = models.CharField(max_length=4, verbose_name='method')
    phastcons = models.FloatField(default=0.0, verbose_name='phastcons')
    Repeat = models.CharField(max_length=6, verbose_name='Repeat')
    Element = models.CharField(max_length=30, verbose_name='Element')
    GeneRegion = models.CharField(max_length=30, verbose_name='GeneRegion')
    AAChange = models.CharField(max_length=20, verbose_name='AAChange')
    Cellline = models.TextField(verbose_name='Cellline')
    Sequence = models.CharField(max_length=250, verbose_name=u'Sequence')
    Editlevel = models.FloatField(default=0.0, verbose_name='Editlevel')
    lncRNA = models.TextField(null=True, blank=True, verbose_name='lncRNA')
    circRNA = models.TextField(null=True, blank=True, verbose_name='circRNA')
    miRNA = models.TextField(null=True, blank=True, verbose_name='miRNA')
    piRNA = models.TextField(null=True, blank=True, verbose_name='piRNA')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"addtime")

    class Meta:
        verbose_name = u"Rat_Rnaedit"
        verbose_name_plural = verbose_name
        unique_together = ('Chr', 'position',)

    def __unicode__(self):
        return '{0}-{1}'.format(self.name, self.position)


class Rhesus_Rnaedit(models.Model):
    name = models.CharField(max_length=10, verbose_name="Rnaedit_name")
    Chr = models.CharField(max_length=5, verbose_name=u"Chr")
    position = models.IntegerField(default=0, verbose_name=u"position")
    Genename = models.CharField(max_length=200, null=True, blank=True, db_index=True, verbose_name=u"Genename")
    Genedetail = models.TextField(null=True, blank=True, verbose_name='Genedetail')
    Strand = models.CharField(max_length=1, verbose_name='Strand')
    Ref = models.CharField(max_length=1, choices=(('A','A'),('T','T')), verbose_name='Ref')
    Alt = models.CharField(max_length=1, choices=(('G','G'),('C','C')), verbose_name='Alt')
    dbSNP = models.CharField(max_length=20, null=True, verbose_name='dbSNP')
    method = models.CharField(max_length=4, verbose_name='method')
    Repeat = models.CharField(max_length=6, verbose_name='Repeat')
    Element = models.CharField(max_length=30, verbose_name='Element')
    GeneRegion = models.CharField(max_length=30, verbose_name='GeneRegion')
    AAChange = models.CharField(max_length=20, verbose_name='AAChange')
    Cellline = models.CharField(max_length=200, verbose_name='Cellline')
    Sequence = models.CharField(max_length=250, verbose_name=u'Sequence')
    Editlevel = models.FloatField(default=0.0, verbose_name='Editlevel')
    lncRNA = models.TextField(null=True, blank=True, verbose_name='lncRNA')
    circRNA = models.TextField(null=True, blank=True, verbose_name='circRNA')
    miRNA = models.TextField(null=True, blank=True, verbose_name='miRNA')
    piRNA = models.TextField(null=True, blank=True, verbose_name='piRNA')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"addtime")

    class Meta:
        verbose_name = u"Rhesus_Rnaedit"
        verbose_name_plural = verbose_name
        unique_together = ('Chr', 'position',)

    def __unicode__(self):
        return '{0}-{1}'.format(self.name, self.position)


class Chimpanzee_Rnaedit(models.Model):
    name = models.CharField(max_length=10, verbose_name="Rnaedit_name")
    Chr = models.CharField(max_length=5, verbose_name=u"Chr")
    position = models.IntegerField(default=0, verbose_name=u"position")
    Genename = models.CharField(max_length=200, null=True, blank=True, db_index=True, verbose_name=u"Genename")
    Genedetail = models.TextField(null=True, blank=True, verbose_name='Genedetail')
    Strand = models.CharField(max_length=1, verbose_name='Strand')
    Ref = models.CharField(max_length=1, choices=(('A','A'),('T','T')), verbose_name='Ref')
    Alt = models.CharField(max_length=1, choices=(('G','G'),('C','C')), verbose_name='Alt')
    dbSNP = models.CharField(max_length=20, null=True, verbose_name='dbSNP')
    method = models.CharField(max_length=4, verbose_name='method')
    Repeat = models.CharField(max_length=6, verbose_name='Repeat')
    Element = models.CharField(max_length=30, verbose_name='Element')
    GeneRegion = models.CharField(max_length=30, verbose_name='GeneRegion')
    AAChange = models.CharField(max_length=20, verbose_name='AAChange')
    Cellline = models.CharField(max_length=200, verbose_name='Cellline')
    Sequence = models.CharField(max_length=250, verbose_name=u'Sequence')
    Editlevel = models.FloatField(default=0.0, verbose_name='Editlevel')
    lncRNA = models.TextField(null=True, blank=True, verbose_name='lncRNA')
    circRNA = models.TextField(null=True, blank=True, verbose_name='circRNA')
    miRNA = models.TextField(null=True, blank=True, verbose_name='miRNA')
    piRNA = models.TextField(null=True, blank=True, verbose_name='piRNA')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"addtime")

    class Meta:
        verbose_name = u"Chimpanzee_Rnaedit"
        verbose_name_plural = verbose_name
        unique_together = ('Chr', 'position',)

    def __unicode__(self):
        return '{0}-{1}'.format(self.name, self.position)


class Cbrenneri_Rnaedit(models.Model):
    name = models.CharField(max_length=10, verbose_name="Rnaedit_name")
    Chr = models.CharField(max_length=20, verbose_name=u"Chr")
    position = models.IntegerField(default=0, verbose_name=u"position")
    Strand = models.CharField(max_length=1, verbose_name='Strand')
    Ref = models.CharField(max_length=1, choices=(('A','A'),('T','T')), verbose_name='Ref')
    Alt = models.CharField(max_length=1, choices=(('G','G'),('C','C')), verbose_name='Alt')
    method = models.CharField(max_length=4, verbose_name='method')
    Cellline = models.TextField(verbose_name='Cellline')
    Sequence = models.CharField(max_length=250, verbose_name=u'Sequence')
    Editlevel = models.FloatField(default=0.0, verbose_name='Editlevel')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"addtime")

    class Meta:
        verbose_name = u"Cbrenneri_Rnaedit"
        verbose_name_plural = verbose_name
        unique_together = ('Chr', 'position',)

    def __unicode__(self):
        return '{0}-{1}'.format(self.name, self.position)


        unique_together = ('Chr', 'position',)
class Cbriggsae_Rnaedit(models.Model):
    name = models.CharField(max_length=10, verbose_name="Rnaedit_name")
    Chr = models.CharField(max_length=20, verbose_name=u"Chr")
    position = models.IntegerField(default=0, verbose_name=u"position")
    Strand = models.CharField(max_length=1, verbose_name='Strand')
    Ref = models.CharField(max_length=1, choices=(('A','A'),('T','T')), verbose_name='Ref')
    Alt = models.CharField(max_length=1, choices=(('G','G'),('C','C')), verbose_name='Alt')
    method = models.CharField(max_length=4, verbose_name='method')
    Cellline = models.TextField(verbose_name='Cellline')
    Sequence = models.CharField(max_length=250, verbose_name=u'Sequence')
    Editlevel = models.FloatField(default=0.0, verbose_name='Editlevel')
    Repeat = models.CharField(max_length=6, verbose_name='Repeat')
    Element = models.CharField(max_length=30, verbose_name='Element')
    GeneRegion = models.CharField(max_length=30, verbose_name='GeneRegion')
    AAChange = models.CharField(max_length=20, verbose_name='AAChange')
    Genename = models.CharField(max_length=250, null=True, blank=True, db_index=True, verbose_name=u"Genename")
    Genedetail = models.TextField(null=True, blank=True, verbose_name='Genedetail')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"addtime")

    class Meta:
        verbose_name = u"Cbriggsae_Rnaedit"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}-{1}'.format(self.name, self.position)


class Celegans_Rnaedit(models.Model):
    name = models.CharField(max_length=10, verbose_name="Rnaedit_name")
    Chr = models.CharField(max_length=20, verbose_name=u"Chr")
    position = models.IntegerField(default=0, verbose_name=u"position")
    Strand = models.CharField(max_length=1, verbose_name='Strand')
    Ref = models.CharField(max_length=1, choices=(('A','A'),('T','T')), verbose_name='Ref')
    Alt = models.CharField(max_length=1, choices=(('G','G'),('C','C')), verbose_name='Alt')
    method = models.CharField(max_length=4, verbose_name='method')
    Cellline = models.TextField(verbose_name='Cellline')
    Sequence = models.CharField(max_length=250, verbose_name=u'Sequence')
    Editlevel = models.FloatField(default=0.0, verbose_name='Editlevel')
    Repeat = models.CharField(max_length=6, verbose_name='Repeat')
    Element = models.CharField(max_length=30, verbose_name='Element')
    GeneRegion = models.CharField(max_length=30, verbose_name='GeneRegion')
    AAChange = models.CharField(max_length=20, verbose_name='AAChange')
    Genename = models.CharField(max_length=200, null=True, blank=True, db_index=True, verbose_name=u"Genename")
    Genedetail = models.TextField(null=True, blank=True, verbose_name='Genedetail')
    lncRNA = models.TextField(null=True, blank=True, verbose_name='lncRNA')
    circRNA = models.TextField(null=True, blank=True, verbose_name='circRNA')
    miRNA = models.TextField(null=True, blank=True, verbose_name='miRNA')
    piRNA = models.TextField(null=True, blank=True, verbose_name='piRNA')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"addtime")

    class Meta:
        verbose_name = u"Celegans_Rnaedit"
        verbose_name_plural = verbose_name
        unique_together = ('Chr', 'position',)

    def __unicode__(self):
        return '{0}-{1}'.format(self.name, self.position)


class Cjaponica_Rnaedit(models.Model):
    name = models.CharField(max_length=10, verbose_name="Rnaedit_name")
    Chr = models.CharField(max_length=20, verbose_name=u"Chr")
    position = models.IntegerField(default=0, verbose_name=u"position")
    Strand = models.CharField(max_length=1, verbose_name='Strand')
    Ref = models.CharField(max_length=1, choices=(('A','A'),('T','T')), verbose_name='Ref')
    Alt = models.CharField(max_length=1, choices=(('G','G'),('C','C')), verbose_name='Alt')
    method = models.CharField(max_length=4, verbose_name='method')
    Cellline = models.TextField(verbose_name='Cellline')
    Sequence = models.CharField(max_length=250, verbose_name=u'Sequence')
    Editlevel = models.FloatField(default=0.0, verbose_name='Editlevel')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"addtime")

    class Meta:
        verbose_name = u"japonica_Rnaedit"
        verbose_name_plural = verbose_name
        unique_together = ('Chr', 'position',)

    def __unicode__(self):
        return '{0}-{1}'.format(self.name, self.position)


class Cremanei_Rnaedit(models.Model):
    name = models.CharField(max_length=10, verbose_name="Rnaedit_name")
    Chr = models.CharField(max_length=20, verbose_name=u"Chr")
    position = models.IntegerField(default=0, verbose_name=u"position")
    Strand = models.CharField(max_length=1, verbose_name='Strand')
    Ref = models.CharField(max_length=1, choices=(('A','A'),('T','T')), verbose_name='Ref')
    Alt = models.CharField(max_length=1, choices=(('G','G'),('C','C')), verbose_name='Alt')
    method = models.CharField(max_length=4, verbose_name='method')
    Cellline = models.TextField(verbose_name='Cellline')
    Sequence = models.CharField(max_length=250, verbose_name=u'Sequence')
    Editlevel = models.FloatField(default=0.0, verbose_name='Editlevel')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"addtime")

    class Meta:
        verbose_name = u"Cremanei_Rnaedit"
        verbose_name_plural = verbose_name
        unique_together = ('Chr', 'position',)

    def __unicode__(self):
        return '{0}-{1}'.format(self.name, self.position)


class Dananassae_Rnaedit(models.Model):
    name = models.CharField(max_length=10, verbose_name="Rnaedit_name")
    Chr = models.CharField(max_length=20, verbose_name=u"Chr")
    position = models.IntegerField(default=0, verbose_name=u"position")
    Strand = models.CharField(max_length=1, verbose_name='Strand')
    Ref = models.CharField(max_length=1, choices=(('A','A'),('T','T')), verbose_name='Ref')
    Alt = models.CharField(max_length=1, choices=(('G','G'),('C','C')), verbose_name='Alt')
    method = models.CharField(max_length=4, verbose_name='method')
    Cellline = models.TextField(verbose_name='Cellline')
    Sequence = models.CharField(max_length=250, verbose_name=u'Sequence')
    Editlevel = models.FloatField(default=0.0, verbose_name='Editlevel')
    Repeat = models.CharField(max_length=6, verbose_name='Repeat')
    Element = models.CharField(max_length=30, verbose_name='Element')
    GeneRegion = models.CharField(max_length=30, verbose_name='GeneRegion')
    AAChange = models.CharField(max_length=20, verbose_name='AAChange')
    Genename = models.CharField(max_length=200, null=True, blank=True, db_index=True, verbose_name=u"Genename")
    Genedetail = models.TextField(null=True, blank=True, verbose_name='Genedetail')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"addtime")

    class Meta:
        verbose_name = u"Dananassae_Rnaedit"
        verbose_name_plural = verbose_name
        unique_together = ('Chr', 'position',)


class Dmelanogaster_Rnaedit(models.Model):
    name = models.CharField(max_length=10, verbose_name="Rnaedit_name")
    Chr = models.CharField(max_length=30, verbose_name=u"Chr")
    position = models.IntegerField(default=0, verbose_name=u"position")
    Genename = models.CharField(max_length=100, null=True, blank=True, db_index=True, verbose_name=u"Genename")
    Genedetail = models.TextField(null=True, blank=True, verbose_name='Genedetail')
    Strand = models.CharField(max_length=1, verbose_name='Strand')
    Ref = models.CharField(max_length=1, choices=(('A','A'),('T','T')), verbose_name='Ref')
    Alt = models.CharField(max_length=1, choices=(('G','G'),('C','C')), verbose_name='Alt')
    database = models.CharField(max_length=3, verbose_name='database')
    method = models.CharField(max_length=4, verbose_name='method')
    Repeat = models.CharField(max_length=6, verbose_name='Repeat')
    Element = models.CharField(max_length=30, verbose_name='Element')
    GeneRegion = models.CharField(max_length=30, verbose_name='GeneRegion')
    AAChange = models.CharField(max_length=20, verbose_name='AAChange')
    Cellline = models.TextField(verbose_name='Cellline')
    Sequence = models.CharField(max_length=250, verbose_name=u'Sequence')
    Editlevel = models.FloatField(default=0.0, verbose_name='Editlevel')
    lncRNA = models.TextField(null=True, blank=True, verbose_name='lncRNA')
    circRNA = models.TextField(null=True, blank=True, verbose_name='circRNA')
    miRNA = models.TextField(null=True, blank=True, verbose_name='miRNA')
    piRNA = models.TextField(null=True, blank=True, verbose_name='piRNA')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"addtime")

    class Meta:
        verbose_name = u"Dmelanogaster_Rnaedit"
        verbose_name_plural = verbose_name
        unique_together = ('Chr', 'position',)

    def __unicode__(self):
        return '{0}-{1}'.format(self.name, self.position)


class Dmojavensis_Rnaedit(models.Model):
    name = models.CharField(max_length=10, verbose_name="Rnaedit_name")
    Chr = models.CharField(max_length=20, verbose_name=u"Chr")
    position = models.IntegerField(default=0, verbose_name=u"position")
    Genename = models.CharField(max_length=100, null=True, blank=True, db_index=True, verbose_name=u"Genename")
    Genedetail = models.TextField(null=True, blank=True, verbose_name='Genedetail')
    Strand = models.CharField(max_length=1, verbose_name='Strand')
    Ref = models.CharField(max_length=1, choices=(('A','A'),('T','T')), verbose_name='Ref')
    Alt = models.CharField(max_length=1, choices=(('G','G'),('C','C')), verbose_name='Alt')
    method = models.CharField(max_length=4, verbose_name='method')
    GeneRegion = models.CharField(max_length=30, verbose_name='GeneRegion')
    AAChange = models.CharField(max_length=20, verbose_name='AAChange')
    Cellline = models.TextField(verbose_name='Cellline')
    Sequence = models.CharField(max_length=250, verbose_name=u'Sequence')
    Editlevel = models.FloatField(default=0.0, verbose_name='Editlevel')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"addtime")

    class Meta:
        verbose_name = u"Dmojavensis_Rnaedit"
        verbose_name_plural = verbose_name
        unique_together = ('Chr', 'position',)

    def __unicode__(self):
        return '{0}-{1}'.format(self.name, self.position)


class Dpseudoobscura_Rnaedit(models.Model):
    name = models.CharField(max_length=10, verbose_name="Rnaedit_name")
    Chr = models.CharField(max_length=30, verbose_name=u"Chr")
    position = models.IntegerField(default=0, verbose_name=u"position")
    Genename = models.CharField(max_length=100, null=True, blank=True, db_index=True, verbose_name=u"Genename")
    Genedetail = models.TextField(null=True, blank=True, verbose_name='Genedetail')
    Strand = models.CharField(max_length=1, verbose_name='Strand')
    Ref = models.CharField(max_length=1, choices=(('A','A'),('T','T')), verbose_name='Ref')
    Alt = models.CharField(max_length=1, choices=(('G','G'),('C','C')), verbose_name='Alt')
    method = models.CharField(max_length=4, verbose_name='method')
    Repeat = models.CharField(max_length=6, verbose_name='Repeat')
    Element = models.CharField(max_length=30, verbose_name='Element')
    GeneRegion = models.CharField(max_length=30, verbose_name='GeneRegion')
    AAChange = models.CharField(max_length=20, verbose_name='AAChange')
    Cellline = models.TextField(verbose_name='Cellline')
    Sequence = models.CharField(max_length=250, verbose_name=u'Sequence')
    Editlevel = models.FloatField(default=0.0, verbose_name='Editlevel')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"addtime")

    class Meta:
        verbose_name = u"Dpseudoobscura_Rnaedit"
        verbose_name_plural = verbose_name
        unique_together = ('Chr', 'position',)

    def __unicode__(self):
        return '{0}-{1}'.format(self.name, self.position)


class Dsimulans_Rnaedit(models.Model):
    name = models.CharField(max_length=10, verbose_name="Rnaedit_name")
    Chr = models.CharField(max_length=20, verbose_name=u"Chr")
    position = models.IntegerField(default=0, verbose_name=u"position")
    Genename = models.CharField(max_length=100, null=True, blank=True, db_index=True, verbose_name=u"Genename")
    Genedetail = models.TextField(null=True, blank=True, verbose_name='Genedetail')
    Strand = models.CharField(max_length=1, verbose_name='Strand')
    Ref = models.CharField(max_length=1, choices=(('A','A'),('T','T')), verbose_name='Ref')
    Alt = models.CharField(max_length=1, choices=(('G','G'),('C','C')), verbose_name='Alt')
    method = models.CharField(max_length=4, verbose_name='method')
    Repeat = models.CharField(max_length=6, verbose_name='Repeat')
    Element = models.CharField(max_length=30, verbose_name='Element')
    GeneRegion = models.CharField(max_length=30, verbose_name='GeneRegion')
    AAChange = models.CharField(max_length=20, verbose_name='AAChange')
    Cellline = models.TextField(verbose_name='Cellline')
    Sequence = models.CharField(max_length=250, verbose_name=u'Sequence')
    Editlevel = models.FloatField(default=0.0, verbose_name='Editlevel')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"addtime")

    class Meta:
        verbose_name = u"Dsimulans_Rnaedit"
        verbose_name_plural = verbose_name
        unique_together = ('Chr', 'position',)

    def __unicode__(self):
        return '{0}-{1}'.format(self.name, self.position)


class Dvirilis_Rnaedit(models.Model):
    name = models.CharField(max_length=10, verbose_name="Rnaedit_name")
    Chr = models.CharField(max_length=20, verbose_name=u"Chr")
    position = models.IntegerField(default=0, verbose_name=u"position")
    Genename = models.CharField(max_length=100, null=True, blank=True, db_index=True, verbose_name=u"Genename")
    Genedetail = models.TextField(null=True, blank=True, verbose_name='Genedetail')
    Strand = models.CharField(max_length=1, verbose_name='Strand')
    Ref = models.CharField(max_length=1, choices=(('A','A'),('T','T')), verbose_name='Ref')
    Alt = models.CharField(max_length=1, choices=(('G','G'),('C','C')), verbose_name='Alt')
    method = models.CharField(max_length=4, verbose_name='method')
    GeneRegion = models.CharField(max_length=30, verbose_name='GeneRegion')
    AAChange = models.CharField(max_length=20, verbose_name='AAChange')
    Cellline = models.TextField(verbose_name='Cellline')
    Sequence = models.CharField(max_length=250, verbose_name=u'Sequence')
    Editlevel = models.FloatField(default=0.0, verbose_name='Editlevel')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"addtime")

    class Meta:
        verbose_name = u"Dvirilis_Rnaedit"
        verbose_name_plural = verbose_name
        unique_together = ('Chr', 'position',)

    def __unicode__(self):
        return '{0}-{1}'.format(self.name, self.position)


class Dyakuba_Rnaedit(models.Model):
    name = models.CharField(max_length=10, verbose_name="Rnaedit_name")
    Chr = models.CharField(max_length=20, verbose_name=u"Chr")
    position = models.IntegerField(default=0, verbose_name=u"position")
    Genename = models.CharField(max_length=100, null=True, blank=True, db_index=True, verbose_name=u"Genename")
    Genedetail = models.TextField(null=True, blank=True, verbose_name='Genedetail')
    Strand = models.CharField(max_length=1, verbose_name='Strand')
    Ref = models.CharField(max_length=1, choices=(('A','A'),('T','T')), verbose_name='Ref')
    Alt = models.CharField(max_length=1, choices=(('G','G'),('C','C')), verbose_name='Alt')
    method = models.CharField(max_length=4, verbose_name='method')
    Repeat = models.CharField(max_length=6, verbose_name='Repeat')
    Element = models.CharField(max_length=30, verbose_name='Element')
    GeneRegion = models.CharField(max_length=30, verbose_name='GeneRegion')
    AAChange = models.CharField(max_length=20, verbose_name='AAChange')
    Cellline = models.TextField(verbose_name='Cellline')
    Sequence = models.CharField(max_length=250, verbose_name=u'Sequence')
    Editlevel = models.FloatField(default=0.0, verbose_name='Editlevel')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"addtime")

    class Meta:
        verbose_name = u"Dyakuba_Rnaedit"
        verbose_name_plural = verbose_name
        unique_together = ('Chr', 'position',)

    def __unicode__(self):
        return '{0}-{1}'.format(self.name, self.position)
