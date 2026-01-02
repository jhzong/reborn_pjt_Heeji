from django.db import models
# from member.models import MyUser

# class Location(models.Model):
#     locno = models.AutoField(primary_key=True)
#     loc_nm = models.CharField(max_length=50, null=True)
#     is_main = models.CharField(max_length=1, default="n", null=True)
#     sort = models.IntegerField(default=0)

#     def __str__(self):
#         return f"{self.locno},{self.loc},{self.is_main},{self.sort}"


# class LocationDetail(models.Model):
#     locdno = models.AutoField(primary_key=True)
#     location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
#     locd_nm = models.CharField(max_length=50, null=True)
#     is_main = models.CharField(max_length=1, null=True)
#     sort = models.IntegerField(default=0)

#     def __str__(self):
#         return f"{self.locdno},{self.location_id},{self.locd_nm},{self.is_main},{self.sort}"



# class FoodType(models.Model):
#     ftypeno = models.AutoField(primary_key=True)
#     ftype = models.CharField(max_length=50, null=True)
#     img_url_main = models.TextField(blank=True, null=True)
#     is_main = models.CharField(max_length=1, default="n", null=True)
#     sort = models.IntegerField(default=0)

#     def __str__(self):
#         return f"{self.ftypeno},{self.ftype},{self.is_main},{self.sort}"


# class Restaurant(models.Model):
#     resno = models.AutoField(primary_key=True)
#     locationDetail = models.ForeignKey(LocationDetail, on_delete=models.SET_NULL, null=True, blank=True)
#     location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
#     res_nm = models.CharField(max_length=50, null=True)
#     desc = models.TextField(blank=True, null=True)
#     addr = models.CharField(max_length=200, null=True)
#     tel = models.CharField(max_length=13, null=True)
#     lat = models.DecimalField(max_digits=10, decimal_places=7, default=0)
#     lng = models.DecimalField(max_digits=10, decimal_places=7, default=0)
#     date = models.DateTimeField(auto_now=True)
#     member = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, blank=True)

#     def __str__(self):
#         return f"{self.resno},{self.res_nm},{self.tel},{self.member.mem_id}"


# class RestaurantOperTime(models.Model):
#     opno = models.AutoField(primary_key=True)
#     resno = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, blank=True)
#     locationDetail = models.ForeignKey(LocationDetail, on_delete=models.SET_NULL, null=True, blank=True)
#     location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
#     week = models.CharField(max_length=50, null=True)
#     open_time = models.TimeField(null=True)
#     close_time = models.TimeField(null=True)
#     desc = models.TextField(blank=True, null=True)
#     date = models.DateTimeField(auto_now=True)
#     member = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, blank=True)

#     def __str__(self):
#         return f"{self.opno},{self.resno_id},{self.week},{self.open_time},{self.close_time},{self.member.mem_id}"


# class FoodMenu(models.Model):
#     fno = models.AutoField(primary_key=True)
#     resno = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, blank=True)
#     locationDetail = models.ForeignKey(LocationDetail, on_delete=models.SET_NULL, null=True, blank=True)
#     location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
#     foodType = models.ForeignKey(FoodType, on_delete=models.SET_NULL, null=True, blank=True)
#     price = models.IntegerField(default=0)
#     fnm = models.CharField(max_length=100, null=True)
#     date = models.DateTimeField(auto_now=True)
#     member = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, blank=True)

#     def __str__(self):
#         return f"{self.fno},{self.fnm},{self.price},{self.member.mem_id}"


# class Img(models.Model):
#     imgno = models.AutoField(primary_key=True)
#     foodMenu = models.ForeignKey(FoodMenu, on_delete=models.SET_NULL, null=True, blank=True)
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, blank=True)
#     location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
#     locationDetail = models.ForeignKey(LocationDetail, on_delete=models.SET_NULL, null=True, blank=True)
#     img_url = models.TextField(null=True)
#     img_nm = models.CharField(max_length=100, null=True)
#     date = models.DateTimeField(auto_now=True)
#     member = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, blank=True)

#     def __str__(self):
#         return f"{self.imgno},{self.img_nm},{self.member.mem_id}"


# class Comment(models.Model):
#     cno = models.AutoField(primary_key=True)
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, blank=True)
#     location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
#     locationDetail = models.ForeignKey(LocationDetail, on_delete=models.SET_NULL, null=True, blank=True)
#     ccontent = models.TextField(null=True)
#     rating = models.DecimalField(max_digits=10, decimal_places=7, default=0)
#     date = models.DateTimeField(auto_now=True)
#     member = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, blank=True)

#     def __str__(self):
#         return f"{self.cno},{self.restaurant.res_nm},{self.ccontent},{self.rating},{self.date},{self.member.mem_id}"
        
class Restaurant(models.Model):
    resno=models.AutoField(primary_key=True)
    locno=models.IntegerField(default=0)
    res_name=models.CharField(max_length=50,null=True)
    desc=models.TextField(null=True)
    addr=models.CharField(max_length=200,null=True)
    tel=models.CharField(max_length=13,null=True)
    lat=models.DecimalField(max_digits=10,decimal_places=7,default=0)
    lng=models.DecimalField(max_digits=10,decimal_places=7,default=0)
    date=models.DateTimeField(auto_now=True)
    mem_id=models.CharField(max_length=25,null=True)
    
    def __str__(self):
        return f"{self.resno},{self.res_name},{self.tel},{self.mem_id}"