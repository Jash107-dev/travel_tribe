// Hunt Feature - Comprehensive Indian Tourism Database (50+ Destinations)
(function() {
  'use strict';
  const huntDatabase = {
    // ANDHRA PRADESH & TELANGANA
    'vizag': { name: 'Visakhapatnam', state: 'Andhra Pradesh', places: [
      { name: 'RK Beach', desc: 'Popular beach with water sports' }, { name: 'Kailasagiri', desc: 'Hill park with cable car' }, { name: 'Borra Caves', desc: 'Ancient natural caves' }, { name: 'Araku Valley', desc: 'Coffee plantations' }, { name: 'Submarine Museum', desc: 'INS Kursura museum' }, { name: 'Simhachalam Temple', desc: 'Lord Narasimha temple' }, { name: 'Yarada Beach', desc: 'Pristine beach' }, { name: 'Dolphin Nose', desc: 'Rocky headland' }],
      foods: [{ name: 'Bamboo Chicken', desc: 'Tribal delicacy' }, { name: 'Pesarattu', desc: 'Green gram dosa' }, { name: 'Gongura Mutton', desc: 'Sorrel leaves curry' }, { name: 'Pootharekulu', desc: 'Paper-thin sweet' }, { name: 'Bobbatlu', desc: 'Sweet flatbread' }, { name: 'Ulava Charu', desc: 'Horse gram soup' }, { name: 'Araku Coffee', desc: 'Organic coffee' }, { name: 'Bongulo Chicken', desc: 'Spicy curry' }]},
    'tirupati': { name: 'Tirupati', state: 'Andhra Pradesh', places: [
      { name: 'Tirumala Temple', desc: 'Richest temple in world' }, { name: 'Padmavathi Temple', desc: 'Goddess temple' }, { name: 'Chandragiri Fort', desc: 'Historic fort' }, { name: 'Talakona Waterfall', desc: 'Highest in AP' }, { name: 'Silathoranam', desc: 'Natural arch' }, { name: 'Zoo Park', desc: 'Wildlife sanctuary' }, { name: 'Kapila Theertham', desc: 'Waterfall temple' }, { name: 'ISKCON Temple', desc: 'Spiritual center' }],
      foods: [{ name: 'Tirupati Laddu', desc: 'Temple prasadam' }, { name: 'Pulihora', desc: 'Tamarind rice' }, { name: 'Pongal', desc: 'Rice lentil dish' }, { name: 'Vada', desc: 'Lentil fritters' }, { name: 'Dosa', desc: 'Rice crepe' }, { name: 'Idli', desc: 'Steamed cakes' }, { name: 'Sambar', desc: 'Lentil stew' }, { name: 'Coconut Chutney', desc: 'Side dish' }]},
    'hyderabad': { name: 'Hyderabad', state: 'Telangana', places: [
      { name: 'Charminar', desc: 'Iconic monument' }, { name: 'Golconda Fort', desc: 'Historic fort' }, { name: 'Hussain Sagar', desc: 'Buddha statue lake' }, { name: 'Ramoji Film City', desc: 'Largest studio' }, { name: 'Salar Jung Museum', desc: 'Art museum' }, { name: 'Chowmahalla Palace', desc: 'Nizam palace' }, { name: 'Birla Mandir', desc: 'Marble temple' }, { name: 'Nehru Zoo', desc: 'Wildlife park' }],
      foods: [{ name: 'Hyderabadi Biryani', desc: 'Famous rice dish' }, { name: 'Haleem', desc: 'Meat wheat stew' }, { name: 'mundi', desc: 'authentic arabian style mundi'}, { name: 'Double Ka Meetha', desc: 'Bread pudding' }, { name: 'Osmania Biscuits', desc: 'Tea biscuits' }, { name: 'Irani Chai', desc: 'Strong tea' }, { name: 'Lukhmi', desc: 'Meat pastry' }, { name: 'Qubani Ka Meetha', desc: 'Apricot dessert' },{ name: 'arabian grill mundi', desc: 'mundi with grill chicken ,luckys biriyani kompally' }]},
    
    // HIMACHAL PRADESH
    'manali': { name: 'Manali', state: 'Himachal Pradesh', places: [
      { name: 'Rohtang Pass', desc: 'Snow activities' }, { name: 'Solang Valley', desc: 'Adventure sports' }, { name: 'Hadimba Temple', desc: 'Wooden temple' }, { name: 'Old Manali', desc: 'Hippie village' }, { name: 'Jogini Waterfall', desc: 'Trekking spot' }, { name: 'Vashisht Hot Springs', desc: 'Natural springs' }, { name: 'Manu Temple', desc: 'Sage temple' }, { name: 'Mall Road', desc: 'Shopping street' }],
      foods: [{ name: 'Siddu', desc: 'Steamed bread' }, { name: 'Dham', desc: 'Festive meal' }, { name: 'Trout Fish', desc: 'River fish' }, { name: 'Babru', desc: 'Stuffed kachori' }, { name: 'Aktori', desc: 'Festive cake' }, { name: 'Tudkiya Bhath', desc: 'Himachali pulao' }, { name: 'Chha Gosht', desc: 'Lamb curry' }, { name: 'Mittha', desc: 'Sweet rice' }]},
    'shimla': { name: 'Shimla', state: 'Himachal Pradesh', places: [
      { name: 'The Ridge', desc: 'Central open space' }, { name: 'Mall Road', desc: 'Shopping street' }, { name: 'Jakhu Temple', desc: 'Hanuman temple' }, { name: 'Christ Church', desc: 'Historic church' }, { name: 'Kufri', desc: 'Hill station' }, { name: 'Viceregal Lodge', desc: 'British building' }, { name: 'Scandal Point', desc: 'Meeting point' }, { name: 'Summer Hill', desc: 'Scenic area' }],
      foods: [{ name: 'Chana Madra', desc: 'Chickpea yogurt' }, { name: 'Siddu', desc: 'Steamed bread' }, { name: 'Babru', desc: 'Kachori' }, { name: 'Tudkiya Bhath', desc: 'Pulao' }, { name: 'Chha Gosht', desc: 'Lamb gravy' }, { name: 'Patande', desc: 'Sweet pancakes' }, { name: 'Aktori', desc: 'Cake' }, { name: 'Apple Pie', desc: 'Local apples' }]},
    'dharamshala': { name: 'Dharamshala', state: 'Himachal Pradesh', places: [
      { name: 'Dalai Lama Temple', desc: 'Residence of Dalai Lama' }, { name: 'Bhagsu Waterfall', desc: 'Popular waterfall' }, { name: 'Triund Trek', desc: 'Famous trek' }, { name: 'McLeod Ganj', desc: 'Tibetan settlement' }, { name: 'Namgyal Monastery', desc: 'Largest Tibetan temple' }, { name: 'Dal Lake', desc: 'Scenic lake' }, { name: 'Kangra Fort', desc: 'Ancient fort' }, { name: 'Tea Gardens', desc: 'Tea plantations' }],
      foods: [{ name: 'Momos', desc: 'Tibetan dumplings' }, { name: 'Thukpa', desc: 'Noodle soup' }, { name: 'Tingmo', desc: 'Steamed bread' }, { name: 'Butter Tea', desc: 'Traditional tea' }, { name: 'Thenthuk', desc: 'Hand-pulled noodles' }, { name: 'Shapta', desc: 'Stir-fried meat' }, { name: 'Khambir', desc: 'Local bread' }, { name: 'Tibetan Bread', desc: 'Fried bread' }]},
    
    // GOA
    'goa': { name: 'Goa', state: 'Goa', places: [
      { name: 'Baga Beach', desc: 'Water sports and nightlife' }, { name: 'Fort Aguada', desc: 'Portuguese fort' }, { name: 'Dudhsagar Falls', desc: 'Four-tiered waterfall' }, { name: 'Old Goa Churches', desc: 'UNESCO heritage' }, { name: 'Anjuna Flea Market', desc: 'Wednesday market' }, { name: 'Palolem Beach', desc: 'Crescent beach' }, { name: 'Spice Plantations', desc: 'Aromatic farms' }, { name: 'Chapora Fort', desc: 'Historic fort' }],
      foods: [{ name: 'Fish Curry Rice', desc: 'Coconut fish curry' }, { name: 'Vindaloo', desc: 'Spicy pork curry' }, { name: 'Bebinca', desc: 'Layered dessert' }, { name: 'Xacuti', desc: 'Complex curry' }, { name: 'Sorpotel', desc: 'Spicy pork dish' }, { name: 'Prawn Balchão', desc: 'Tangy prawn pickle' }, { name: 'Sanna', desc: 'Steamed rice cakes' }, { name: 'Feni', desc: 'Local liquor' }]},
    
    // UTTAR PRADESH
    'varanasi': { name: 'Varanasi', state: 'Uttar Pradesh', places: [
      { name: 'Dashashwamedh Ghat', desc: 'Main ghat with Aarti' }, { name: 'Kashi Vishwanath', desc: 'Sacred Shiva temple' }, { name: 'Assi Ghat', desc: 'Southern ghat' }, { name: 'Sarnath', desc: 'Buddhist site' }, { name: 'Manikarnika Ghat', desc: 'Cremation ghat' }, { name: 'Ramnagar Fort', desc: '18th-century fort' }, { name: 'BHU', desc: 'University campus' }, { name: 'Boat Ride', desc: 'Sunrise on Ganges' }],
      foods: [{ name: 'Kachori Sabzi', desc: 'Crispy kachori' }, { name: 'Banarasi Paan', desc: 'Betel leaf' }, { name: 'Chaat', desc: 'Street food' }, { name: 'Malaiyo', desc: 'Frothy milk dessert' }, { name: 'Tamatar Chaat', desc: 'Tomato chaat' }, { name: 'Launglata', desc: 'Sweet pretzel' }, { name: 'Baati Chokha', desc: 'Baked wheat balls' }, { name: 'Rabri', desc: 'Thickened milk' }]},
    'agra': { name: 'Agra', state: 'Uttar Pradesh', places: [
      { name: 'Taj Mahal', desc: 'Wonder of the world' }, { name: 'Agra Fort', desc: 'Red sandstone fort' }, { name: 'Fatehpur Sikri', desc: 'Abandoned Mughal city' }, { name: 'Mehtab Bagh', desc: 'Taj view garden' }, { name: 'Itimad-ud-Daulah', desc: 'Baby Taj' }, { name: 'Akbar Tomb', desc: 'Mughal emperor tomb' }, { name: 'Jama Masjid', desc: 'Large mosque' }, { name: 'Wildlife SOS', desc: 'Bear rescue center' }],
      foods: [{ name: 'Petha', desc: 'Sweet pumpkin candy' }, { name: 'Bedai', desc: 'Spicy kachori' }, { name: 'Dalmoth', desc: 'Spicy snack mix' }, { name: 'Paratha', desc: 'Stuffed flatbread' }, { name: 'Chaat', desc: 'Street food' }, { name: 'Jalebi', desc: 'Sweet spirals' }, { name: 'Lassi', desc: 'Yogurt drink' }, { name: 'Mughlai Cuisine', desc: 'Rich curries' }]},
    'lucknow': { name: 'Lucknow', state: 'Uttar Pradesh', places: [
      { name: 'Bara Imambara', desc: 'Architectural marvel' }, { name: 'Chota Imambara', desc: 'Palace of lights' }, { name: 'Rumi Darwaza', desc: 'Turkish gate' }, { name: 'British Residency', desc: 'Historical ruins' }, { name: 'Hazratganj', desc: 'Shopping area' }, { name: 'Ambedkar Park', desc: 'Memorial park' }, { name: 'Lucknow Zoo', desc: 'Wildlife park' }, { name: 'Janeshwar Mishra Park', desc: 'Large park' }],
      foods: [{ name: 'Tunday Kababi', desc: 'Melt-in-mouth kebabs' }, { name: 'Lucknowi Biryani', desc: 'Awadhi biryani' }, { name: 'Kakori Kebab', desc: 'Soft kebabs' }, { name: 'Sheermal', desc: 'Saffron bread' }, { name: 'Kulfi Faluda', desc: 'Ice cream dessert' }, { name: 'Basket Chaat', desc: 'Potato basket' }, { name: 'Malai Makhan', desc: 'Creamy dessert' }, { name: 'Nihari', desc: 'Slow-cooked stew' }]},
    
    // LADAKH & JAMMU KASHMIR
    'ladakh': { name: 'Ladakh', state: 'Ladakh (UT)', places: [
      { name: 'Pangong Lake', desc: 'Stunning blue lake' }, { name: 'Nubra Valley', desc: 'Cold desert' }, { name: 'Leh Palace', desc: '17th-century palace' }, { name: 'Magnetic Hill', desc: 'Gravity-defying hill' }, { name: 'Thiksey Monastery', desc: 'Beautiful monastery' }, { name: 'Khardung La', desc: 'Highest motorable pass' }, { name: 'Tso Moriri Lake', desc: 'High-altitude lake' }, { name: 'Hemis Monastery', desc: 'Largest monastery' }],
      foods: [{ name: 'Thukpa', desc: 'Noodle soup' }, { name: 'Momos', desc: 'Tibetan dumplings' }, { name: 'Skyu', desc: 'Pasta-like dish' }, { name: 'Butter Tea', desc: 'Salted tea' }, { name: 'Tingmo', desc: 'Steamed bread' }, { name: 'Chhurpi', desc: 'Yak cheese' }, { name: 'Khambir', desc: 'Wheat bread' }, { name: 'Apricot Jam', desc: 'Local apricots' }]},
    'srinagar': { name: 'Srinagar', state: 'Jammu & Kashmir', places: [
      { name: 'Dal Lake', desc: 'Houseboats and shikaras' }, { name: 'Mughal Gardens', desc: 'Shalimar, Nishat' }, { name: 'Shankaracharya Temple', desc: 'Hilltop temple' }, { name: 'Hazratbal Shrine', desc: 'White marble mosque' }, { name: 'Pari Mahal', desc: 'Garden of fairies' }, { name: 'Tulip Garden', desc: 'Asia\'s largest' }, { name: 'Nigeen Lake', desc: 'Quieter lake' }, { name: 'Old City', desc: 'Historic markets' }],
      foods: [{ name: 'Rogan Josh', desc: 'Aromatic lamb curry' }, { name: 'Wazwan', desc: 'Multi-course meal' }, { name: 'Kahwa', desc: 'Kashmiri green tea' }, { name: 'Gushtaba', desc: 'Minced mutton balls' }, { name: 'Yakhni', desc: 'Yogurt-based curry' }, { name: 'Modur Pulav', desc: 'Sweet rice' }, { name: 'Nadru Yakhni', desc: 'Lotus stem curry' }, { name: 'Sheermal', desc: 'Saffron bread' }]},
    
    // RAJASTHAN
    'jaipur': { name: 'Jaipur', state: 'Rajasthan', places: [
      { name: 'Hawa Mahal', desc: 'Palace of winds' }, { name: 'Amber Fort', desc: 'Majestic fort' }, { name: 'City Palace', desc: 'Royal residence' }, { name: 'Jantar Mantar', desc: 'Observatory' }, { name: 'Jal Mahal', desc: 'Water palace' }, { name: 'Nahargarh Fort', desc: 'City views' }, { name: 'Albert Hall', desc: 'Oldest museum' }, { name: 'Jaigarh Fort', desc: 'Largest cannon' }],
      foods: [{ name: 'Dal Baati Churma', desc: 'Baked wheat balls' }, { name: 'Laal Maas', desc: 'Red mutton curry' }, { name: 'Ghewar', desc: 'Disc-shaped sweet' }, { name: 'Pyaaz Kachori', desc: 'Onion kachori' }, { name: 'Mirchi Vada', desc: 'Chili fritters' }, { name: 'Ker Sangri', desc: 'Desert beans curry' }, { name: 'Mawa Kachori', desc: 'Sweet kachori' }, { name: 'Lassi', desc: 'Yogurt drink' }]},
    'udaipur': { name: 'Udaipur', state: 'Rajasthan', places: [
      { name: 'City Palace', desc: 'Palace on lake' }, { name: 'Lake Pichola', desc: 'Scenic lake' }, { name: 'Jag Mandir', desc: 'Island palace' }, { name: 'Saheliyon Ki Bari', desc: 'Garden of maidens' }, { name: 'Fateh Sagar Lake', desc: 'Artificial lake' }, { name: 'Monsoon Palace', desc: 'Hilltop palace' }, { name: 'Bagore Ki Haveli', desc: 'Cultural shows' }, { name: 'Jagdish Temple', desc: 'Vishnu temple' }],
      foods: [{ name: 'Dal Baati Churma', desc: 'Traditional meal' }, { name: 'Gatte Ki Sabzi', desc: 'Gram flour curry' }, { name: 'Mawa Kachori', desc: 'Sweet kachori' }, { name: 'Laal Maas', desc: 'Spicy mutton' }, { name: 'Mirchi Bada', desc: 'Chili fritters' }, { name: 'Dahi Vada', desc: 'Lentil in yogurt' }, { name: 'Malpua', desc: 'Sweet pancakes' }, { name: 'Rajasthani Thali', desc: 'Complete meal' }]},
    'jodhpur': { name: 'Jodhpur', state: 'Rajasthan', places: [
      { name: 'Mehrangarh Fort', desc: 'Massive hilltop fort' }, { name: 'Jaswant Thada', desc: 'Marble cenotaph' }, { name: 'Umaid Bhawan', desc: 'Palace hotel' }, { name: 'Clock Tower', desc: 'Market area' }, { name: 'Mandore Gardens', desc: 'Historic gardens' }, { name: 'Rao Jodha Park', desc: 'Desert park' }, { name: 'Toorji Ka Jhalra', desc: 'Stepwell' }, { name: 'Blue City', desc: 'Blue-painted houses' }],
      foods: [{ name: 'Mirchi Vada', desc: 'Stuffed chilies' }, { name: 'Pyaaz Kachori', desc: 'Onion pastry' }, { name: 'Mawa Kachori', desc: 'Sweet kachori' }, { name: 'Makhaniya Lassi', desc: 'Creamy lassi' }, { name: 'Dal Baati', desc: 'Wheat balls with dal' }, { name: 'Gatte Ki Sabzi', desc: 'Gram flour curry' }, { name: 'Ker Sangri', desc: 'Desert vegetables' }, { name: 'Malpua', desc: 'Sweet pancakes' }]},
    
    // KERALA
    'kerala': { name: 'Kerala', state: 'Kerala', places: [
      { name: 'Alleppey Backwaters', desc: 'Houseboat cruises' }, { name: 'Munnar', desc: 'Tea plantations' }, { name: 'Kovalam Beach', desc: 'Crescent beach' }, { name: 'Periyar Sanctuary', desc: 'Tiger reserve' }, { name: 'Fort Kochi', desc: 'Chinese fishing nets' }, { name: 'Wayanad', desc: 'Hill district' }, { name: 'Varkala Beach', desc: 'Cliff beach' }, { name: 'Athirapally Falls', desc: 'Largest waterfall' }],
      foods: [{ name: 'Appam Stew', desc: 'Rice pancake curry' }, { name: 'Kerala Sadya', desc: 'Feast on banana leaf' }, { name: 'Fish Moilee', desc: 'Mild fish curry' }, { name: 'Puttu Kadala', desc: 'Rice cake chickpea' }, { name: 'Karimeen Pollichathu', desc: 'Pearl spot fish' }, { name: 'Banana Chips', desc: 'Fried banana' }, { name: 'Payasam', desc: 'Sweet pudding' }, { name: 'Beef Fry', desc: 'Spicy fried beef' }]},
    'kochi': { name: 'Kochi (Cochin)', state: 'Kerala', places: [
      { name: 'Fort Kochi', desc: 'Colonial architecture' }, { name: 'Chinese Fishing Nets', desc: 'Iconic nets' }, { name: 'Mattancherry Palace', desc: 'Dutch Palace' }, { name: 'Jewish Synagogue', desc: 'Oldest synagogue' }, { name: 'Marine Drive', desc: 'Waterfront promenade' }, { name: 'Bolgatty Palace', desc: 'Island palace' }, { name: 'Hill Palace', desc: 'Archaeological museum' }, { name: 'Kathakali Center', desc: 'Traditional dance' }],
      foods: [{ name: 'Appam', desc: 'Rice pancake' }, { name: 'Fish Curry', desc: 'Coconut fish curry' }, { name: 'Puttu', desc: 'Steamed rice cake' }, { name: 'Idiyappam', desc: 'String hoppers' }, { name: 'Prawn Curry', desc: 'Spicy prawn dish' }, { name: 'Banana Chips', desc: 'Crispy snack' }, { name: 'Payasam', desc: 'Sweet dessert' }, { name: 'Seafood Platter', desc: 'Fresh catch' }]},
    
    // UTTARAKHAND
    'rishikesh': { name: 'Rishikesh', state: 'Uttarakhand', places: [
      { name: 'Laxman Jhula', desc: 'Suspension bridge' }, { name: 'Ram Jhula', desc: 'Famous bridge' }, { name: 'Triveni Ghat', desc: 'Evening aarti' }, { name: 'Beatles Ashram', desc: 'Graffiti art' }, { name: 'Neer Garh Waterfall', desc: 'Trekking spot' }, { name: 'Parmarth Niketan', desc: 'Yoga ashram' }, { name: 'Rajaji National Park', desc: 'Wildlife sanctuary' }, { name: 'Kunjapuri Temple', desc: 'Sunrise views' }],
      foods: [{ name: 'Aloo Puri', desc: 'Fried bread potato' }, { name: 'Chole Bhature', desc: 'Chickpea curry' }, { name: 'Kachori', desc: 'Stuffed pastry' }, { name: 'Lassi', desc: 'Yogurt drink' }, { name: 'Fruit Salad', desc: 'Fresh fruits' }, { name: 'Momos', desc: 'Dumplings' }, { name: 'Thali', desc: 'Vegetarian meal' }, { name: 'Herbal Tea', desc: 'Himalayan tea' }]},
    'nainital': { name: 'Nainital', state: 'Uttarakhand', places: [
      { name: 'Naini Lake', desc: 'Pear-shaped lake' }, { name: 'Naina Devi Temple', desc: 'Lakeside temple' }, { name: 'Mall Road', desc: 'Shopping street' }, { name: 'Tiffin Top', desc: 'Viewpoint' }, { name: 'Snow View Point', desc: 'Himalayan views' }, { name: 'Eco Cave Gardens', desc: 'Interconnected caves' }, { name: 'Nainital Zoo', desc: 'High-altitude zoo' }, { name: 'Bhimtal Lake', desc: 'Nearby lake' }],
      foods: [{ name: 'Bal Mithai', desc: 'Chocolate fudge' }, { name: 'Singori', desc: 'Coconut sweet' }, { name: 'Aloo Ke Gutke', desc: 'Spicy potatoes' }, { name: 'Bhatt Ki Churkani', desc: 'Black bean curry' }, { name: 'Ras', desc: 'Lentil curry' }, { name: 'Dubuk', desc: 'Lentil dish' }, { name: 'Gulgula', desc: 'Sweet fritters' }, { name: 'Kumaoni Raita', desc: 'Yogurt dish' }]},
    
    // PUNJAB
    'amritsar': { name: 'Amritsar', state: 'Punjab', places: [
      { name: 'Golden Temple', desc: 'Holiest Sikh shrine' }, { name: 'Jallianwala Bagh', desc: 'Memorial garden' }, { name: 'Wagah Border', desc: 'Flag ceremony' }, { name: 'Partition Museum', desc: '1947 partition' }, { name: 'Durgiana Temple', desc: 'Hindu temple' }, { name: 'Gobindgarh Fort', desc: 'Historic fort' }, { name: 'Ram Bagh', desc: 'Historic garden' }, { name: 'Ranjit Singh Museum', desc: 'Palace museum' }],
      foods: [{ name: 'Amritsari Kulcha', desc: 'Stuffed bread' }, { name: 'Lassi', desc: 'Creamy yogurt drink' }, { name: 'Makki Di Roti', desc: 'Corn bread' }, { name: 'Amritsari Fish', desc: 'Crispy fried fish' }, { name: 'Chole Bhature', desc: 'Chickpea curry' }, { name: 'Jalebi', desc: 'Sweet spirals' }, { name: 'Pinni', desc: 'Wheat sweet' }, { name: 'Langar', desc: 'Free meal' }]},
    
    // TAMIL NADU
    'chennai': { name: 'Chennai', state: 'Tamil Nadu', places: [
      { name: 'Marina Beach', desc: 'Second longest beach' }, { name: 'Kapaleeshwarar Temple', desc: 'Dravidian architecture' }, { name: 'Fort St. George', desc: 'First English fortress' }, { name: 'San Thome Cathedral', desc: 'Gothic church' }, { name: 'Government Museum', desc: 'Bronze gallery' }, { name: 'Mahabalipuram', desc: 'Shore temple' }, { name: 'Valluvar Kottam', desc: 'Monument' }, { name: 'Elliot Beach', desc: 'Clean beach' }],
      foods: [{ name: 'Idli Sambar', desc: 'Steamed cakes' }, { name: 'Dosa', desc: 'Crispy crepe' }, { name: 'Chettinad Chicken', desc: 'Spicy curry' }, { name: 'Filter Coffee', desc: 'South Indian coffee' }, { name: 'Pongal', desc: 'Rice lentil dish' }, { name: 'Vada', desc: 'Lentil fritters' }, { name: 'Biryani', desc: 'Ambur biryani' }, { name: 'Payasam', desc: 'Sweet pudding' }]},
    'madurai': { name: 'Madurai', state: 'Tamil Nadu', places: [
      { name: 'Meenakshi Temple', desc: 'Iconic temple towers' }, { name: 'Thirumalai Nayak Palace', desc: 'Indo-Saracenic palace' }, { name: 'Gandhi Museum', desc: 'Freedom struggle' }, { name: 'Alagar Kovil', desc: 'Hill temple' }, { name: 'Vandiyur Mariamman', desc: 'Temple tank' }, { name: 'Koodal Azhagar Temple', desc: 'Vishnu temple' }, { name: 'Samanar Hills', desc: 'Jain caves' }, { name: 'Puthu Mandapam', desc: 'Pillar hall' }],
      foods: [{ name: 'Jigarthanda', desc: 'Cold milk drink' }, { name: 'Paruthi Paal', desc: 'Cotton seed milk' }, { name: 'Kari Dosa', desc: 'Minced meat dosa' }, { name: 'Idiyappam', desc: 'String hoppers' }, { name: 'Chettinad Cuisine', desc: 'Spicy dishes' }, { name: 'Paniyaram', desc: 'Sweet dumplings' }, { name: 'Murukku', desc: 'Crispy snack' }, { name: 'Halwa', desc: 'Sweet dessert' }]},
    
    // KARNATAKA
    'bangalore': { name: 'Bangalore', state: 'Karnataka', places: [
      { name: 'Lalbagh Garden', desc: 'Botanical garden' }, { name: 'Cubbon Park', desc: 'Green lung' }, { name: 'Bangalore Palace', desc: 'Tudor-style palace' }, { name: 'ISKCON Temple', desc: 'Krishna temple' }, { name: 'Tipu Sultan Palace', desc: 'Wooden palace' }, { name: 'Vidhana Soudha', desc: 'Legislative building' }, { name: 'Nandi Hills', desc: 'Hill station' }, { name: 'Bannerghatta Park', desc: 'Zoo and safari' }],
      foods: [{ name: 'Masala Dosa', desc: 'Crispy dosa' }, { name: 'Bisi Bele Bath', desc: 'Rice lentil dish' }, { name: 'Ragi Mudde', desc: 'Finger millet balls' }, { name: 'Mysore Pak', desc: 'Gram flour sweet' }, { name: 'Idli Vada', desc: 'Breakfast combo' }, { name: 'Filter Coffee', desc: 'South Indian coffee' }, { name: 'Puliyogare', desc: 'Tamarind rice' }, { name: 'Holige', desc: 'Sweet flatbread' }]},
    'mysore': { name: 'Mysore', state: 'Karnataka', places: [
      { name: 'Mysore Palace', desc: 'Indo-Saracenic palace' }, { name: 'Chamundi Hills', desc: 'Temple on hill' }, { name: 'Brindavan Gardens', desc: 'Musical fountain' }, { name: 'St. Philomena Church', desc: 'Neo-Gothic church' }, { name: 'Mysore Zoo', desc: 'Oldest zoo' }, { name: 'Jaganmohan Palace', desc: 'Art gallery' }, { name: 'Rail Museum', desc: 'Heritage trains' }, { name: 'Karanji Lake', desc: 'Bird sanctuary' }],
      foods: [{ name: 'Mysore Pak', desc: 'Famous sweet' }, { name: 'Mysore Masala Dosa', desc: 'Red chutney dosa' }, { name: 'Bisi Bele Bath', desc: 'Spicy rice dish' }, { name: 'Ragi Mudde', desc: 'Millet balls' }, { name: 'Holige', desc: 'Sweet bread' }, { name: 'Chitranna', desc: 'Lemon rice' }, { name: 'Kesari Bath', desc: 'Semolina sweet' }, { name: 'Filter Coffee', desc: 'Decoction coffee' }]},
    
    // MAHARASHTRA
    'mumbai': { name: 'Mumbai', state: 'Maharashtra', places: [
      { name: 'Gateway of India', desc: 'Iconic monument' }, { name: 'Marine Drive', desc: 'Queen\'s necklace' }, { name: 'Elephanta Caves', desc: 'Rock-cut temples' }, { name: 'Chhatrapati Terminus', desc: 'UNESCO railway station' }, { name: 'Haji Ali Dargah', desc: 'Mosque on sea' }, { name: 'Juhu Beach', desc: 'Popular beach' }, { name: 'Siddhivinayak Temple', desc: 'Ganesh temple' }, { name: 'Colaba Causeway', desc: 'Shopping street' }],
      foods: [{ name: 'Vada Pav', desc: 'Potato burger' }, { name: 'Pav Bhaji', desc: 'Mashed vegetables' }, { name: 'Misal Pav', desc: 'Spicy sprouts' }, { name: 'Bhel Puri', desc: 'Puffed rice snack' }, { name: 'Sev Puri', desc: 'Crispy chaat' }, { name: 'Bombay Sandwich', desc: 'Vegetable sandwich' }, { name: 'Keema Pav', desc: 'Minced meat' }, { name: 'Modak', desc: 'Sweet dumpling' }]},
    'pune': { name: 'Pune', state: 'Maharashtra', places: [
      { name: 'Shaniwar Wada', desc: 'Historic fortification' }, { name: 'Aga Khan Palace', desc: 'Gandhi memorial' }, { name: 'Sinhagad Fort', desc: 'Hill fort' }, { name: 'Osho Ashram', desc: 'Meditation center' }, { name: 'Dagdusheth Temple', desc: 'Ganesh temple' }, { name: 'Parvati Hill', desc: 'Temple complex' }, { name: 'Pune Okayama Park', desc: 'Japanese garden' }, { name: 'Raja Dinkar Kelkar', desc: 'Art museum' }],
      foods: [{ name: 'Misal Pav', desc: 'Spicy sprouts curry' }, { name: 'Mastani', desc: 'Thick milkshake' }, { name: 'Bhakarwadi', desc: 'Spicy roll' }, { name: 'Puran Poli', desc: 'Sweet flatbread' }, { name: 'Vada Pav', desc: 'Potato fritter' }, { name: 'Pithla Bhakri', desc: 'Gram flour curry' }, { name: 'Sabudana Khichdi', desc: 'Tapioca dish' }, { name: 'Shrikhand', desc: 'Sweetened yogurt' }]},
    
    // WEST BENGAL
    'kolkata': { name: 'Kolkata', state: 'West Bengal', places: [
      { name: 'Victoria Memorial', desc: 'White marble building' }, { name: 'Howrah Bridge', desc: 'Iconic cantilever bridge' }, { name: 'Dakshineswar Temple', desc: 'Kali temple' }, { name: 'Indian Museum', desc: 'Oldest museum' }, { name: 'Kalighat Temple', desc: 'Shakti Peetha' }, { name: 'Park Street', desc: 'Food and nightlife' }, { name: 'Science City', desc: 'Interactive museum' }, { name: 'Marble Palace', desc: 'Neoclassical mansion' }],
      foods: [{ name: 'Rosogolla', desc: 'Spongy sweet balls' }, { name: 'Mishti Doi', desc: 'Sweet yogurt' }, { name: 'Fish Curry', desc: 'Bengali fish curry' }, { name: 'Kosha Mangsho', desc: 'Spicy mutton' }, { name: 'Luchi Alur Dom', desc: 'Fried bread potato' }, { name: 'Sandesh', desc: 'Milk sweet' }, { name: 'Puchka', desc: 'Pani puri' }, { name: 'Kathi Roll', desc: 'Wrap rolls' }]},
    'darjeeling': { name: 'Darjeeling', state: 'West Bengal', places: [
      { name: 'Tiger Hill', desc: 'Sunrise viewpoint' }, { name: 'Darjeeling Toy Train', desc: 'UNESCO heritage train' }, { name: 'Batasia Loop', desc: 'Railway loop' }, { name: 'Peace Pagoda', desc: 'Buddhist stupa' }, { name: 'Himalayan Zoo', desc: 'High-altitude zoo' }, { name: 'Tea Gardens', desc: 'Famous tea estates' }, { name: 'Observatory Hill', desc: 'Temple and views' }, { name: 'Rock Garden', desc: 'Terraced garden' }],
      foods: [{ name: 'Momos', desc: 'Tibetan dumplings' }, { name: 'Thukpa', desc: 'Noodle soup' }, { name: 'Darjeeling Tea', desc: 'World-famous tea' }, { name: 'Churpee', desc: 'Yak cheese' }, { name: 'Sha Phaley', desc: 'Meat bread' }, { name: 'Tingmo', desc: 'Steamed bread' }, { name: 'Gundruk', desc: 'Fermented greens' }, { name: 'Sel Roti', desc: 'Rice doughnut' }]},
    
    // GUJARAT
    'ahmedabad': { name: 'Ahmedabad', state: 'Gujarat', places: [
      { name: 'Sabarmati Ashram', desc: 'Gandhi\'s residence' }, { name: 'Adalaj Stepwell', desc: 'Intricate stepwell' }, { name: 'Akshardham Temple', desc: 'Grand temple' }, { name: 'Kankaria Lake', desc: 'Recreational lake' }, { name: 'Sidi Saiyyed Mosque', desc: 'Jali work' }, { name: 'Calico Museum', desc: 'Textile museum' }, { name: 'Jama Masjid', desc: 'Yellow sandstone mosque' }, { name: 'Auto World Museum', desc: 'Vintage cars' }],
      foods: [{ name: 'Dhokla', desc: 'Steamed gram flour cake' }, { name: 'Khandvi', desc: 'Rolled gram flour' }, { name: 'Thepla', desc: 'Spiced flatbread' }, { name: 'Fafda Jalebi', desc: 'Crispy snack sweet' }, { name: 'Undhiyu', desc: 'Mixed vegetable curry' }, { name: 'Khaman', desc: 'Soft dhokla' }, { name: 'Dabeli', desc: 'Spicy burger' }, { name: 'Mohanthal', desc: 'Gram flour sweet' }]},
    'surat': { name: 'Surat', state: 'Gujarat', places: [
      { name: 'Dumas Beach', desc: 'Black sand beach' }, { name: 'Surat Castle', desc: 'Historic fort' }, { name: 'Science Centre', desc: 'Interactive exhibits' }, { name: 'Dutch Garden', desc: 'Colonial cemetery' }, { name: 'Sardar Patel Museum', desc: 'History museum' }, { name: 'Gopi Talav', desc: 'Lake and garden' }, { name: 'Suvali Beach', desc: 'Clean beach' }, { name: 'Textile Market', desc: 'Fabric shopping' }],
      foods: [{ name: 'Locho', desc: 'Steamed snack' }, { name: 'Surati Ghari', desc: 'Sweet disc' }, { name: 'Undhiyu', desc: 'Winter vegetable mix' }, { name: 'Ponk Vada', desc: 'Sorghum fritters' }, { name: 'Khaman', desc: 'Gram flour snack' }, { name: 'Surati Khaja', desc: 'Layered sweet' }, { name: 'Rasawala Khaman', desc: 'Dhokla in gravy' }, { name: 'Pani Puri', desc: 'Crispy shells' }]},
    
    // ODISHA
    'puri': { name: 'Puri', state: 'Odisha', places: [
      { name: 'Jagannath Temple', desc: 'Sacred Hindu temple' }, { name: 'Puri Beach', desc: 'Golden sand beach' }, { name: 'Konark Sun Temple', desc: 'UNESCO heritage' }, { name: 'Chilika Lake', desc: 'Largest coastal lagoon' }, { name: 'Raghurajpur', desc: 'Artisan village' }, { name: 'Gundicha Temple', desc: 'Rath Yatra destination' }, { name: 'Narendra Tank', desc: 'Sacred pond' }, { name: 'Loknath Temple', desc: 'Shiva temple' }],
      foods: [{ name: 'Mahaprasad', desc: 'Temple offering' }, { name: 'Chhena Poda', desc: 'Baked cheese cake' }, { name: 'Dalma', desc: 'Lentil vegetable stew' }, { name: 'Pakhala', desc: 'Fermented rice' }, { name: 'Rasagola', desc: 'Spongy sweet' }, { name: 'Khaja', desc: 'Layered sweet' }, { name: 'Chhena Gaja', desc: 'Fried cheese sweet' }, { name: 'Machha Besara', desc: 'Fish mustard curry' }]},
    
    // ASSAM
    'guwahati': { name: 'Guwahati', state: 'Assam', places: [
      { name: 'Kamakhya Temple', desc: 'Shakti Peetha temple' }, { name: 'Brahmaputra River', desc: 'River cruise' }, { name: 'Umananda Island', desc: 'Peacock island' }, { name: 'Assam State Museum', desc: 'Cultural artifacts' }, { name: 'Pobitora Sanctuary', desc: 'Rhino sanctuary' }, { name: 'Navagraha Temple', desc: 'Nine planets temple' }, { name: 'Srimanta Sankardev', desc: 'Cultural center' }, { name: 'Dipor Bil', desc: 'Bird sanctuary' }],
      foods: [{ name: 'Assam Tea', desc: 'World-famous tea' }, { name: 'Masor Tenga', desc: 'Sour fish curry' }, { name: 'Khar', desc: 'Alkaline dish' }, { name: 'Pitha', desc: 'Rice cakes' }, { name: 'Duck Curry', desc: 'Spicy duck' }, { name: 'Aloo Pitika', desc: 'Mashed potato' }, { name: 'Laksa', desc: 'Sweet dessert' }, { name: 'Bamboo Shoot', desc: 'Fermented shoots' }]},
    
    // MADHYA PRADESH
    'bhopal': { name: 'Bhopal', state: 'Madhya Pradesh', places: [
      { name: 'Upper Lake', desc: 'Largest artificial lake' }, { name: 'Taj-ul-Masajid', desc: 'Largest mosque in India' }, { name: 'Sanchi Stupa', desc: 'Buddhist monument' }, { name: 'Bhimbetka Caves', desc: 'Rock shelters' }, { name: 'Van Vihar', desc: 'National park' }, { name: 'Gohar Mahal', desc: 'Lakeside palace' }, { name: 'Bhojpur Temple', desc: 'Incomplete temple' }, { name: 'State Museum', desc: 'Tribal art' }],
      foods: [{ name: 'Poha Jalebi', desc: 'Flattened rice sweet' }, { name: 'Bhutte Ka Kees', desc: 'Grated corn dish' }, { name: 'Dal Bafla', desc: 'Wheat balls with dal' }, { name: 'Mawa Bati', desc: 'Sweet dumplings' }, { name: 'Kebabs', desc: 'Mughlai kebabs' }, { name: 'Biryani', desc: 'Bhopali biryani' }, { name: 'Sabudana Khichdi', desc: 'Tapioca dish' }, { name: 'Lavang Lata', desc: 'Clove pastry' }]},
    
    // BIHAR
    'patna': { name: 'Patna', state: 'Bihar', places: [
      { name: 'Mahabodhi Temple', desc: 'Buddha enlightenment site' }, { name: 'Nalanda University', desc: 'Ancient university ruins' }, { name: 'Patna Sahib', desc: 'Sikh pilgrimage' }, { name: 'Golghar', desc: 'Granary with views' }, { name: 'Patna Museum', desc: 'Mauryan artifacts' }, { name: 'Gandhi Maidan', desc: 'Historic ground' }, { name: 'Kumhrar', desc: 'Archaeological site' }, { name: 'Sanjay Gandhi Park', desc: 'Botanical garden' }],
      foods: [{ name: 'Litti Chokha', desc: 'Roasted wheat balls' }, { name: 'Sattu Paratha', desc: 'Gram flour bread' }, { name: 'Khaja', desc: 'Layered sweet' }, { name: 'Tilkut', desc: 'Sesame sweet' }, { name: 'Chana Ghugni', desc: 'Chickpea curry' }, { name: 'Malpua', desc: 'Sweet pancakes' }, { name: 'Thekua', desc: 'Fried sweet' }, { name: 'Mutton Curry', desc: 'Spicy mutton' }]},
    
    // CHHATTISGARH
    'raipur': { name: 'Raipur', state: 'Chhattisgarh', places: [
      { name: 'Mahant Ghasidas Museum', desc: 'Tribal artifacts' }, { name: 'Nandan Van Zoo', desc: 'Safari park' }, { name: 'Vivekananda Sarovar', desc: 'Lake and park' }, { name: 'Purkhouti Muktangan', desc: 'Tribal culture' }, { name: 'Chitrakote Falls', desc: 'Niagara of India' }, { name: 'Barnawapara Sanctuary', desc: 'Wildlife reserve' }, { name: 'Ghatarani Waterfalls', desc: 'Picnic spot' }, { name: 'Mahakoshal Art Gallery', desc: 'Art museum' }],
      foods: [{ name: 'Chila', desc: 'Rice pancake' }, { name: 'Farra', desc: 'Steamed snack' }, { name: 'Aamat', desc: 'Mixed vegetable curry' }, { name: 'Bafauri', desc: 'Steamed lentil cakes' }, { name: 'Dehati Chicken', desc: 'Country chicken curry' }, { name: 'Muthia', desc: 'Steamed dumplings' }, { name: 'Kusli', desc: 'Sweet dish' }, { name: 'Petha', desc: 'Pumpkin sweet' }]},
    
    // JHARKHAND
    'ranchi': { name: 'Ranchi', state: 'Jharkhand', places: [
      { name: 'Hundru Falls', desc: 'Spectacular waterfall' }, { name: 'Tagore Hill', desc: 'Rabindranath Tagore spot' }, { name: 'Rock Garden', desc: 'Artistic rock formations' }, { name: 'Jagannath Temple', desc: 'Replica of Puri temple' }, { name: 'Pahari Mandir', desc: 'Hilltop temple' }, { name: 'Ranchi Lake', desc: 'Boating lake' }, { name: 'Birsa Zoological Park', desc: 'Zoo and safari' }, { name: 'Dassam Falls', desc: 'Scenic waterfall' }],
      foods: [{ name: 'Litti Chokha', desc: 'Roasted wheat balls' }, { name: 'Dhuska', desc: 'Rice lentil pancake' }, { name: 'Rugra', desc: 'Mushroom curry' }, { name: 'Chilka Roti', desc: 'Rice flour bread' }, { name: 'Pitha', desc: 'Rice cakes' }, { name: 'Arsa Roti', desc: 'Sweet rice bread' }, { name: 'Handia', desc: 'Rice beer' }, { name: 'Bamboo Shoot Curry', desc: 'Tribal delicacy' }]},
    
    // NORTHEAST STATES
    'shillong': { name: 'Shillong', state: 'Meghalaya', places: [
      { name: 'Elephant Falls', desc: 'Three-tiered waterfall' }, { name: 'Umiam Lake', desc: 'Scenic reservoir' }, { name: 'Shillong Peak', desc: 'Highest point' }, { name: 'Don Bosco Museum', desc: 'Indigenous cultures' }, { name: 'Ward Lake', desc: 'Horseshoe lake' }, { name: 'Living Root Bridges', desc: 'Natural bridges' }, { name: 'Mawlynnong', desc: 'Cleanest village' }, { name: 'Dawki River', desc: 'Crystal clear water' }],
      foods: [{ name: 'Jadoh', desc: 'Red rice with meat' }, { name: 'Dohneiiong', desc: 'Pork with black sesame' }, { name: 'Tungrymbai', desc: 'Fermented soybean' }, { name: 'Nakham Bitchi', desc: 'Dried fish chutney' }, { name: 'Pumaloi', desc: 'Steamed rice cake' }, { name: 'Minil Songa', desc: 'Sticky rice' }, { name: 'Pukhlein', desc: 'Fried sweet' }, { name: 'Kwai', desc: 'Betel nut' }]},
    'gangtok': { name: 'Gangtok', state: 'Sikkim', places: [
      { name: 'Tsomgo Lake', desc: 'Glacial lake' }, { name: 'Nathula Pass', desc: 'Indo-China border' }, { name: 'Rumtek Monastery', desc: 'Largest monastery' }, { name: 'MG Marg', desc: 'Shopping street' }, { name: 'Hanuman Tok', desc: 'Temple viewpoint' }, { name: 'Banjhakri Falls', desc: 'Waterfall and park' }, { name: 'Enchey Monastery', desc: 'Buddhist monastery' }, { name: 'Tashi Viewpoint', desc: 'Kanchenjunga views' }],
      foods: [{ name: 'Momos', desc: 'Steamed dumplings' }, { name: 'Thukpa', desc: 'Noodle soup' }, { name: 'Gundruk', desc: 'Fermented greens' }, { name: 'Sha Phaley', desc: 'Meat bread' }, { name: 'Sael Roti', desc: 'Rice doughnut' }, { name: 'Chhurpi', desc: 'Yak cheese' }, { name: 'Kinema', desc: 'Fermented soybean' }, { name: 'Thenthuk', desc: 'Hand-pulled noodles' }]},
    'imphal': { name: 'Imphal', state: 'Manipur', places: [
      { name: 'Loktak Lake', desc: 'Floating islands' }, { name: 'Kangla Fort', desc: 'Historic fort' }, { name: 'Ima Keithel', desc: 'Women\'s market' }, { name: 'Shri Govindajee Temple', desc: 'Vaishnavite temple' }, { name: 'War Cemetery', desc: 'WWII memorial' }, { name: 'Khonghampat Orchidarium', desc: 'Orchid sanctuary' }, { name: 'Keibul Lamjao Park', desc: 'Floating national park' }, { name: 'Manipur State Museum', desc: 'Cultural museum' }],
      foods: [{ name: 'Eromba', desc: 'Boiled vegetables with fish' }, { name: 'Chamthong', desc: 'Vegetable stew' }, { name: 'Singju', desc: 'Spicy salad' }, { name: 'Nga Thongba', desc: 'Fish curry' }, { name: 'Paaknam', desc: 'Fritters' }, { name: 'Chak-hao Kheer', desc: 'Black rice pudding' }, { name: 'Kangshoi', desc: 'Healthy vegetable soup' }, { name: 'Morok Metpa', desc: 'Chili chutney' }]},
    
    // ANDAMAN & NICOBAR
    'portblair': { name: 'Port Blair', state: 'Andaman & Nicobar', places: [
      { name: 'Cellular Jail', desc: 'Colonial prison' }, { name: 'Radhanagar Beach', desc: 'Asia\'s best beach' }, { name: 'Ross Island', desc: 'Ruins and peacocks' }, { name: 'North Bay Island', desc: 'Water sports' }, { name: 'Baratang Island', desc: 'Limestone caves' }, { name: 'Mahatma Gandhi Park', desc: 'Marine park' }, { name: 'Chidiya Tapu', desc: 'Sunset point' }, { name: 'Anthropological Museum', desc: 'Tribal culture' }],
      foods: [{ name: 'Fish Curry', desc: 'Fresh seafood curry' }, { name: 'Coconut Prawn Curry', desc: 'Creamy prawn dish' }, { name: 'Grilled Lobster', desc: 'Fresh lobster' }, { name: 'Amritsari Kulcha', desc: 'Stuffed bread' }, { name: 'Tandoori Fish', desc: 'Grilled fish' }, { name: 'Coconut Crab', desc: 'Local delicacy' }, { name: 'Banana Chips', desc: 'Crispy snack' }, { name: 'Tropical Fruits', desc: 'Fresh island fruits' }]}
  };

  // Initialize Hunt Feature
  function initHunt() {
    const searchInput = document.getElementById('huntSearchInput');
    const resultsDiv = document.getElementById('huntResults');
    if (!searchInput || !resultsDiv) return;
    searchInput.addEventListener('input', debounce(performSearch, 300));
    function performSearch() {
      const query = searchInput.value.trim().toLowerCase();
      if (query.length < 2) {
        resultsDiv.style.display = 'none';
        return;
      }
      let matchedDestination = null;
      for (const [key, data] of Object.entries(huntDatabase)) {
        if (key.includes(query) || data.name.toLowerCase().includes(query) || data.state.toLowerCase().includes(query)) {
          matchedDestination = data;
          break;
        }
      }
      if (matchedDestination) {
        displayResults(matchedDestination);
      } else {
        displayNoResults(query);
      }
    }
    function displayResults(destination) {
      resultsDiv.style.display = 'block';
      const html = `
        <div class="hunt-results-header">
          <h3><i class="fas fa-map-marker-alt"></i> ${destination.name}</h3>
          <p><i class="fas fa-map"></i> ${destination.state}</p>
        </div>
        <div class="hunt-results-grid">
          <div class="hunt-card">
            <div class="hunt-card-header">
              <div class="hunt-icon"><i class="fas fa-map-marked-alt"></i></div>
              <h4>Must Visit Places</h4>
            </div>
            <ul class="hunt-list">
              ${destination.places.map(place => `
                <li>
                  <i class="fas fa-check-circle"></i>
                  <div class="hunt-item-content">
                    <div class="hunt-item-name">${place.name}</div>
                    <div class="hunt-item-desc">${place.desc}</div>
                  </div>
                </li>
              `).join('')}
            </ul>
          </div>
          <div class="hunt-card">
            <div class="hunt-card-header">
              <div class="hunt-icon"><i class="fas fa-utensils"></i></div>
              <h4>Must Try Foods</h4>
            </div>
            <ul class="hunt-list">
              ${destination.foods.map(food => `
                <li>
                  <i class="fas fa-check-circle"></i>
                  <div class="hunt-item-content">
                    <div class="hunt-item-name">${food.name}</div>
                    <div class="hunt-item-desc">${food.desc}</div>
                  </div>
                </li>
              `).join('')}
            </ul>
          </div>
        </div>
      `;
      resultsDiv.innerHTML = html;
      resultsDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
    function displayNoResults(query) {
      resultsDiv.style.display = 'block';
      const html = `
        <div class="no-results">
          <i class="fas fa-search"></i>
          <h3>No results found for "${query}"</h3>
          <p>Try: Vizag, Hyderabad, Manali, Shimla, Goa, Varanasi, Agra, Lucknow, Ladakh, Srinagar, Jaipur, Udaipur, Jodhpur, Kerala, Kochi, Rishikesh, Nainital, Amritsar, Chennai, Madurai, Bangalore, Mysore, Mumbai, Pune, Kolkata, Darjeeling, Ahmedabad, Surat, Puri, Guwahati, Bhopal, Patna, Raipur, Ranchi, Shillong, Gangtok, Imphal, Port Blair</p>
        </div>
      `;
      resultsDiv.innerHTML = html;
    }
    function debounce(func, wait) {
      let timeout;
      return function executedFunction(...args) {
        const later = () => {
          clearTimeout(timeout);
          func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
      };
    }
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initHunt);
  } else {
    initHunt();
  }
})();
