from django.db import models

# Create your models here.
class results(models.Model):
    national_id = models.CharField(max_length=12)
    grade7_center_number =  models.IntegerField(blank=True, null=True)
    grade7_candidate_number =  models.IntegerField(blank=True, null=True)
    candidate_name = models.CharField(max_length=200, blank=True, null=True)
    grade7_mathematics =  models.IntegerField(blank=True, null=True)
    grade7_english =  models.IntegerField(blank=True, null=True)
    grade7_shona =  models.IntegerField(blank=True, null=True)
    grade7_social_science =  models.IntegerField(blank=True, null=True)
    grade7_science_and_tech =  models.IntegerField(blank=True, null=True)
    grade7_agriculture =  models.IntegerField(blank=True, null=True)
    grade7_certificate = models.ImageField(upload_to ='uploads/',blank=True, null=True)

    olevel_center_number =  models.IntegerField(blank=True, null=True)
    olevel_candidate_number =  models.IntegerField(blank=True, null=True)
    olevel_mathematics =  models.IntegerField(blank=True, null=True)
    olevel_english =  models.IntegerField(blank=True, null=True)
    olevel_shona =  models.IntegerField(blank=True, null=True)
    olevel_history =  models.IntegerField(blank=True, null=True)
    olevel_geography =  models.IntegerField(blank=True, null=True)
    olevel_combined_science =  models.IntegerField(blank=True, null=True)
    olevel_physics =  models.IntegerField(blank=True, null=True)
    olevel_chemistry =  models.IntegerField(blank=True, null=True)
    olevel_biology =  models.IntegerField(blank=True, null=True)
    olevel_literature =  models.IntegerField(blank=True, null=True)
    olevel_accounts =  models.IntegerField(blank=True, null=True)
    olevel_commerce =  models.IntegerField(blank=True, null=True)
    olevel_family_religious_studies = models.IntegerField(blank=True, null=True)
    olevel_arts =  models.IntegerField(blank=True, null=True)
    olevel_computer_science =  models.IntegerField(blank=True, null=True)
    olevel_woodwork =  models.IntegerField(blank=True, null=True)
    olevel_metal_work =  models.IntegerField(blank=True, null=True)
    olevel_technical_graphics =  models.IntegerField(blank=True, null=True)
    olevel_building =  models.IntegerField(blank=True, null=True)
    olevel_food_nutrition =  models.IntegerField(blank=True, null=True)
    olevel_fashion_fabrics =  models.IntegerField(blank=True, null=True)
    olevel_certificate = models.ImageField(upload_to ='uploads/',blank=True, null=True)
    
    alevel_center_number =  models.IntegerField(blank=True, null=True)
    alevel_candidate_number =  models.IntegerField(blank=True, null=True)
    alevel_mathematics =  models.IntegerField(blank=True, null=True)
    alevel_further_mathematics =  models.IntegerField(blank=True, null=True)
    alevel_statistics =  models.IntegerField(blank=True, null=True)
    alevel_accounts =  models.IntegerField(blank=True, null=True)
    alevel_geography =  models.IntegerField(blank=True, null=True)
    alevel_history =  models.IntegerField(blank=True, null=True)
    alevel_chemistry =  models.IntegerField(blank=True, null=True)
    alevel_biology = models.IntegerField(blank=True, null=True)
    alevel_literature =  models.IntegerField(blank=True, null=True)
    alevel_economics =  models.IntegerField(blank=True, null=True)
    alevel_bussiness_studies =  models.IntegerField(blank=True, null=True)
    alevel_crop_science =  models.IntegerField(blank=True, null=True)
    alevel_communication_skills =  models.IntegerField(blank=True, null=True)
    alevel_certificate = models.ImageField(upload_to ='uploads/',blank=True, null=True)


    def __str__(self):
        return str(self.national_id)
    

    
    


