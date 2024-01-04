
import glob

import argparse

from dev_functions import*

from dev_media_spending import*

if __name__== "__main__":
    pass

parser = argparse.ArgumentParser()

parser.add_argument("--tag", help=" laz_aff , laz_search , laz_cpas_fb , laz_cpas_msb_sku , laz_cpas_msb_overview ,  shp_aff , shp_search , shp_cpas_fb ,shp_cpas_msb_sku , shp_cpas_msb_camp , tiki_aff , tiki_search , tiki_cpas_fb , tiki_cpas_msb_camp")    

args = parser.parse_args()

label=str(args.tag)

db='media_spending_raw'

if label=='laz_aff':
    
    p=glob.glob('data/platform_lazada/affiliate/raw/*')
    
    p.sort()
    
    laz_aff(db,p,label)


elif label=='laz_search':

    p=glob.glob('data/platform_lazada/search/raw/*')

    p.sort()

    laz_search(db,p,label)


# elif label=='laz_cpas_fb':

#     p=glob.glob('data/platform_lazada/cpas/fb/raw/*')
   
#     p.sort()

#     laz_cpas_fb(db,p,label)


# elif label=='laz_cpas_msb_sku':

#     p=glob.glob('data/platform_lazada/cpas/msb/raw/*')

#     p.sort()

#     laz_cpas_msb_sku(db,p,label)
    

# elif label=='laz_cpas_msb_overview':
    
#     p=glob.glob('data/platform_lazada/cpas/msb/raw/*')
    
#     p.sort()
    
#     laz_cpas_msb_overview(db,p,label)


elif label=='shp_aff':
    
    p=glob.glob('data/platform_shopee/affiliate/raw/*')
    
    p.sort()
    
    shp_aff(db,p,label)


elif label=='shp_search':

    p=glob.glob('data/platform_shopee/search/raw/*')

    p.sort()

    shp_search(db,p,label)


# elif label=='shp_cpas_fb':

#     p=glob.glob('data/platform_shopee/cpas/fb/raw/*')
   
#     p.sort()

#     shp_cpas_fb(db,p,label)


# elif label=='shp_cpas_msb_sku':

#     p=glob.glob('data/platform_shopee/cpas/msb/raw/sku/*')

#     p.sort()

#     shp_cpas_msb_sku(db,p,label)
    

# elif label=='shp_cpas_msb_camp':
    
#     p=glob.glob('data/platform_shopee/cpas/msb/raw/campaign/*')
    
#     p.sort()
    
#     shp_cpas_msb_camp(db,p,label)


elif label=='tiki_aff':
    
    p=glob.glob('data/platform_tiki/affiliate/raw/*')
    
    p.sort()
    
    tiki_aff(db,p,label)


elif label=='tiki_search':

    p=glob.glob('data/platform_tiki/search/raw/*')

    p.sort()

    tiki_search(db,p,label)


# elif label=='tiki_cpas_fb':

#     p=glob.glob('data/platform_tiki/cpas/fb/raw/*')
   
#     p.sort()

#     tiki_cpas_fb(db,p,label)


# elif label=='tiki_cpas_msb_camp':

#     p=glob.glob('data/platform_tiki/cpas/msb/raw/*')

#     p.sort()

#     tiki_cpas_msb_camp(db,p,label)


else:
    
    pass

