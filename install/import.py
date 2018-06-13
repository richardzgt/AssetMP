import csv
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AssetMP.settings")


import django

if django.VERSION >= (1, 7): 
    django.setup()


def main():
    from AssetMP.models import Platform,Asset,IDC,AssetStatus,ManType,MachineType
    reader = csv.reader(open("/data/AssetMP/asset.csv"))
    

    Asset.objects.all().delete() #clean db

    for idc,platform,manufacturer,machine_type,uhight,railnum,cabinet,hostname,ipadd,manager_ip,remote_card_ip,product_name,serial_number,suppliers,cpu,disk,memory,status,confirm in reader:
        if confirm == "y":
            print (hostname,Platform.objects.get(name=platform),ManType.objects.get(name=manufacturer),MachineType.objects.get(name=machine_type),IDC.objects.get(name=idc))

            Asset.objects.create(serial_number=serial_number,idc=IDC.objects.get(name=idc),platform=Platform.objects.get(name=platform),manufacturer=ManType.objects.get(name=manufacturer),machine_type=MachineType.objects.get(name=machine_type),uhight=uhight,railnum=railnum,cabinet=cabinet,hostname=hostname,ipadd=ipadd,manager_ip=manager_ip,remote_card_ip=remote_card_ip,product_name=product_name,suppliers=suppliers,cpu=cpu,disk=disk,memory=memory,status=AssetStatus.objects.get(name=status))



if __name__ == "__main__":
    main()
    print('Done!')
