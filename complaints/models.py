from django.db import models

class Villagename(models.Model):
    snno = models.PositiveIntegerField(db_column='snNo', blank=True, null=True)  # Field name made lowercase.
    villagename = models.CharField(db_column='villageName', primary_key=True, max_length=45)  # Field name made lowercase.

    class Meta:
        db_table = 'villagename'


class Complaints(models.Model):
    slno = models.PositiveIntegerField(db_column='slNo')  # Field name made lowercase.
    complainno = models.CharField(db_column='complainNo', primary_key=True, max_length=10)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    subject = models.CharField(max_length=450)
    villagename = models.ForeignKey('Villagename', models.DO_NOTHING, db_column='villageName')  # Field name made lowercase.        
    actionby = models.CharField(db_column='actionBy', max_length=45, blank=True, null=True)  # Field name made lowercase.
    status = models.TextField( blank=True, null=True)
    #status = models.CharField(max_length=10, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    
    def __str__(self):
        return self.complainno
    class Meta:
        db_table = 'complaints'


