import pytrends
import seaborn as sns
import pandas as pd

from pytrends.request import TrendReq

pytrends = TrendReq(hl='es-LA', tz=360)

#kw_list = ["inmigrar+EEUU","inmigrar+españa","asilo+EEUU","asilo+españa","inmigrar","EEUU","emigrar"]
kw_list = ["solicitante","llegada","asilo","ciudadania","consulado","aduana","deportacion","diaspora","embajada","emigrante","emigrar","emigracion","extranjero","ilegal","inmigrante","inmigrar","inmigracion","legalizacion","migrante","migrar","migracion","nacionalidad","naturalizacion","pasaporte","cuota","refugiado","traficante","turista","indocumentado","visa","EEUU","españa"]

# do u.s., spain, mexico, colombia
geo_list = [
			"PA", # panama
			"EC", # ecuador
			"CL", # chile
			"CO", # colombia
			"CU", # cuba
			"DM", # dominica
			"SV", # el salvador
			"GT", # guatemala
			"MX", # mexico
			"NI", # nicaragua
			"PE", # peru
			"VE", # venezuela
			"HN", # honduras
			"CR", # costa rica
			"GD", # granada
			]


frame_list = []

# returns wee
for item in geo_list:
	for word in kw_list:
		pytrends.build_payload([word], timeframe='today 5-y', geo=item, gprop='')
		frame_ = pytrends.interest_over_time()
		frame_['Country Code'] = item
		frame_['word'] = word
		print(frame_)
		frame_list.append(frame_)


full_frame = pd.concat(frame_list).reset_index()
full_frame.to_csv('gtrends_all.csv', index=False)

