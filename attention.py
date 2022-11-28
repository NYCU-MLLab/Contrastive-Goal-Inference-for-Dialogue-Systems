import numpy as np
import matplotlib
import matplotlib.pylab as plt
import seaborn as sns


# attmap = np.load("./attention/028.npy")
# uniform_data = attmap.T[[32,35,36,37,38,39,33,42,43,44,45,46,48,49,50,51],:]
# y_axis_labels = [
# "the_fitzwilliam_museum address trumpington_street", 
# "the_fitzwilliam_museum area centre", 
# "the_fitzwilliam_museum phone 01223332900", 
# "the_fitzwilliam_museum postcode cb21rb", 
# "the_fitzwilliam_museum pricerange free", 
# "the_fitzwilliam_museum type museum", 
# "broughton_house_gallery address 98_king_street",
# "broughton_house_gallery area centre", 
# "broughton_house_gallery phone 01223314960", 
# "broughton_house_gallery type museum",
# "regency_gallery address 39_fitzroy_street", 
# "regency_gallery area centre", 
# "regency_gallery phone 01223365454", 
# "regency_gallery postcode cb11er", 
# "regency_gallery pricerange free", 
# "regency_gallery type museum",
# ]

# attmap = np.load("./attention/021.npy")
# uniform_data = attmap.T[[29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,26,48],:]
# y_axis_labels = [
# "pizza_hut_city_centre area centre",
# "pizza_hut_city_centre food italian",
# "pizza_hut_city_centre phone 01223323737",
# "pizza_hut_city_centre postcode cb21ab",
# "pizza_hut_city_centre pricerange cheap",
# "pizza_hut_city_centre type restaurant",
# "prezzo address 21_-_24_northampton_road",
# "prezzo area west",
# "prezzo food italian",
# "prezzo phone 01799521260",
# "prezzo postcode cb30ad",
# "prezzo pricerange moderate",
# "prezzo type restaurant",
# "da_vinci_pizzeria address 20_milton_road_chesterton",
# "da_vinci_pizzeria area north",
# "da_vinci_pizzeria food italian",
# "da_vinci_pizzeria phone 01223351707",
# "da_vinci_pizzeria postcode cb41jy",
# "da_vinci_pizzeria pricerange cheap",
# "da_vinci_pizzeria type restaurant"
# ]

# attmap = np.load("./attention/075.npy")
# uniform_data = attmap.T[[34,35,36,37,38,7,33,41,42,43,44,45,49,48,46,50,51,52,53],:]
# y_axis_labels = [
# "ashley_hotel address 74_chesterton_road", 
# "ashley_hotel area north", 
# "ashley_hotel phone 01223350059", 
# "ashley_hotel pricerange moderate", 
# "ashley_hotel stars 2_star", 
# "ashley_hotel type hotel",
# "acorn_guest_house area north", 
# "acorn_guest_house phone 01223353888", 
# "acorn_guest_house pricerange moderate", 
# "acorn_guest_house stars 4_star", 
# "alpha-milton_guest_house area north", 
# "alpha-milton_guest_house phone 01223311625", 
# "alpha-milton_guest_house pricerange moderate", 
# "alpha-milton_guest_house stars 3_star", 
# "lovell_lodge address 365_milton_road",
# "lovell_lodge area north", 
# "lovell_lodge pricerange moderate", 
# "lovell_lodge stars 2_star", 
# "lovell_lodge type hotel",
# ]

# attmap = np.load("./attention/002.npy")
# uniform_data = attmap.T[[25,26,27,28,29,30,31,32,33,34,35,36,37,38,41,41,40,42,43,44,45,46,],:]
# y_axis_labels = [
# "danville saturday dry", 
# "danville saturday_low 80f", 
# "danville saturday_high 90f", 
# "danville sunday overcast", 
# "danville sunday_low 20f", 
# "danville sunday_high 30f", 
# "alhambra monday rain", 
# "alhambra monday_low 80f", 
# "alhambra monday_high 100f",  
# "alhambra wednesday foggy", 
# "alhambra wednesday_low 90f", 
# "alhambra thursday_low 90f", 
# "alhambra thursday_high 100f", 
# "alhambra friday clear_skies", 
# "alhambra friday_low 20f", 
# "alhambra friday_high 30f", 
# "alhambra saturday drizzle", 
# "alhambra saturday_low 30f", 
# "alhambra saturday_high 40f", 
# "alhambra sunday stormy", 
# "alhambra sunday_low 90f", 
# "alhambra sunday_high 100f",  
# ]

attmap = np.load("./attention/202.npy")
uniform_data = attmap.T[[13, 12, 11, 16, 17, 18, 19, 20, 21, 22, 23, 15, 14, 26, 23],:]
y_axis_labels = [
"palo_alto_garage_r distance 2_miles", 
"palo_alto_garage_r traffic_info moderate_traffic", 
"parking_garage poi palo_alto_garage_r", 
"jing_jing traffic_info heavy_traffic", 
"jing_jing address 113_arbol_dr", 
"sigona_farmers_market distance 4_miles", 
"sigona_farmers_market traffic_info no_traffic", 
"sigona_farmers_market address 638_amherst_st", 
"grocery_store poi sigona_farmers_market", 
"the_westin distance 4_miles", 
"the_westin traffic_info no_traffic", 
"cafe_venetia distance 4_miles", 
"cafe_venetia traffic_info no_traffic", 
"cafe_venetia address 269_alger_dr",
"coffee_or_tea_place poi cafe_venetia", 
]

x_axis_labels = range(1,len(attmap)+1,1)
ax = sns.heatmap(uniform_data, xticklabels=x_axis_labels, yticklabels=y_axis_labels, cmap="YlGnBu", square=True)


figure = ax.get_figure()
figure.savefig('./attmap/attm_nav.png', dpi=400)




















