
import glob

import argparse

from dev_functions import*

from dev_key_metrics import*

if __name__== "__main__":
    pass

parser = argparse.ArgumentParser()

parser.add_argument("--tag", help="laz_biz , shp_biz , shp_overall ,tiki_seller_center ")    

args = parser.parse_args()

label=str(args.tag)


db='key_metrics_raw'




if label=='laz_biz':
    
    p=glob.glob('data/platform_lazada/business_advisor/raw_new/*/*')
    
    p.sort()
    
    laz_biz(db,p,label)


elif label=='shp_overall':

    p=glob.glob('data/platform_shopee/business_advisor/overall/raw_new/*')

    p.sort()

    shp_overall(db,p,label)


elif label=='shp_biz':

    p=glob.glob('data/platform_shopee/business_advisor/product/raw_new/*')
   
    p.sort()

    shp_biz(db,p,label)


elif label=='tiki_seller_center':

    p=glob.glob('data/platform_tiki/business_advisor/seller_center/raw_new/*')

    p.sort()

    tiki_seller_center(db,p,label)


else:
    
    pass

    

