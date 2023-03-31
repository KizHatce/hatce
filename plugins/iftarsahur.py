# CODED BY :d

from pyrogram import Client, filters
import pytz
from unidecode import unidecode
from datetime import datetime, timedelta
import requests
import re
import logging
from bs4 import BeautifulSoup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)
Hea={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Pragma": "no-cache"
    } 

idjson = {"ADANA":{"ADANA":"9146","ALADAG":"9147","CEYHAN":"9148","FEKE":"9149","IMAMOGLU":"9150","KARAISALI":"9151","KARATAS":"9152","KOZAN":"9153","POZANTI":"9154","SAIMBEYLI":"9155","TUFANBEYLI":"9156","YUMURTALIK":"9157"},"ADIYAMAN":{"ADIYAMAN":"9158","BESNI":"9159","CELIKHAN":"9160","GERGER":"9161","GOLBASI":"9162","KAHTA":"9163","SAMSAT":"9164","SINCIK":"9165","TUT":"9166"},"AFYONKARAHISAR":{"AFYONKARAHISAR":"9167","BASMAKCI":"9168","BAYAT":"9169","BOLVADIN":"9170","CAY":"9171","COBANLAR":"9172","DAZKIRI":"9173","DINAR":"9174","EMIRDAG":"9175","EVCILER":"9176","HOCALAR":"9177","IHSANIYE":"9178","ISCEHISAR":"9179","KIZILOREN":"9180","SANDIKLI":"9181","SINANPASA":"9182","SUHUT":"9183","SULTANDAGI":"9184"},"AGRI":{"AGRI":"9185","DIYADIN":"9186","DOGUBEYAZIT":"9187","ELESKIRT":"9188","PATNOS":"9189","TASLICAY":"9190","TUTAK":"9191"},"AKSARAY":{"AGACOREN":"9192","AKSARAY":"9193","ESKIL":"9194","GULAGAC":"9195","GUZELYURT":"9196","ORTAKOY":"17877","SARIYAHSI":"9197","SULTANHANI":"20069"},"AMASYA":{"AMASYA":"9198","GOYNUCEK":"9199","GUMUSHACIKOY":"9200","HAMAMOZU":"9201","MERZIFON":"9202","SULUOVA":"9203","TASOVA":"9204"},"ANKARA":{"AKYURT":"9205","ANKARA":"9206","AYAS":"9207","BALA":"9208","BEYPAZARI":"9209","CAMLIDERE":"9210","CUBUK":"9211","ELMADAG":"9212","EVREN":"9213","GUDUL":"9214","HAYMANA":"9215","KAHRAMANKAZAN":"9217","KALECIK":"9216","KIZILCAHAMAM":"9218","NALLIHAN":"9219","POLATLI":"9220","SEREFLIKOCHISAR":"9221"},"ANTALYA":{"AKSEKI":"9222","AKSU":"9223","ALANYA":"9224","ANTALYA":"9225","DEMRE":"9226","ELMALI":"9227","FINIKE":"9228","GAZIPASA":"9229","GUNDOGMUS":"9230","IBRADI":"9231","KAS":"9232","KEMER":"9233","KORKUTELI":"9234","KUMLUCA":"9235","MANAVGAT":"9236","SERIK":"9237"},"ARDAHAN":{"ARDAHAN":"9238","CILDIR":"9239","DAMAL":"9240","GOLE":"9241","HANAK":"9242","POSOF":"9243"},"ARTVIN":{"ARDANUC":"9244","ARHAVI":"9245","ARTVIN":"9246","BORCKA":"9247","HOPA":"9248","KEMALPASA":"20070","MURGUL":"9249","SAVSAT":"9250","YUSUFELI":"9251"},"AYDIN":{"AYDIN":"9252","BOZDOGAN":"9253","BUHARKENT":"9254","CINE":"9255","DIDIM":"9256","GERMENCIK":"9257","INCIRLIOVA":"9258","KARACASU":"9259","KARPUZLU":"9260","KOCARLI":"9261","KOSK":"9262","KUSADASI":"9263","KUYUCAK":"9264","NAZILLI":"9265","SOKE":"9266","SULTANHISAR":"9267","YENIPAZAR (A)":"9268"},"BALIKESIR":{"AYVALIK":"9269","BALIKESIR":"9270","BALYA":"9271","BANDIRMA":"17917","BIGADIC":"9272","BURHANIYE":"9273","DURSUNBEY":"9274","EDREMIT":"9275","ERDEK":"17881","GOMEC":"9276","GONEN":"9277","HAVRAN":"9278","IVRINDI":"9279","KEPSUT":"9280","MANYAS":"17918","MARMARA":"9281","SAVASTEPE":"9282","SINDIRGI":"9283","SUSURLUK":"9284"},"BARTIN":{"BARTIN":"9285","KURUCASILE":"9286","ULUS":"9287"},"BATMAN":{"BATMAN":"9288","BESIRI":"9289","GERCUS":"9290","HASANKEYF":"9291","KOZLUK":"9292","SASON":"9293"},"BAYBURT":{"AYDINTEPE":"9294","BAYBURT":"9295","DEMIROZU":"9296"},"BILECIK":{"BILECIK":"9297","BOZUYUK":"9298","GOLPAZARI":"9299","INHISAR":"9300","OSMANELI":"17895","PAZARYERI":"17896","SOGUT":"9301","YENIPAZAR":"9302"},"BINGOL":{"ADAKLI":"17889","BINGOL":"9303","KARLIOVA":"9304","KIGI":"9305","SOLHAN":"9306","YAYLADERE":"9307","YEDISU":"9308"},"BITLIS":{"ADILCEVAZ":"9309","AHLAT":"9310","BITLIS":"9311","GUROYMAK":"17887","HIZAN":"9312","MUTKI":"9313","TATVAN":"9314"},"BOLU":{"BOLU":"9315","DORTDIVAN":"9316","GEREDE":"9317","GOYNUK":"9318","KIBRISCIK":"9319","MENGEN":"9320","MUDURNU":"9321","SEBEN":"9322","YENICAGA":"9323"},"BURDUR":{"AGLASUN":"9324","ALTINYAYLA":"9325","BUCAK":"9326","BURDUR":"9327","CAVDIR":"9328","CELTIKCI":"9329","GOLHISAR":"9330","KARAMANLI":"9331","KEMER (B)":"9332","TEFENNI":"9333","YESILOVA":"9334"},"BURSA":{"BURSA":"9335","BUYUK ORHAN":"9336","GEMLIK":"9337","HARMANCIK":"9338","INEGOL":"9339","IZNIK":"9340","KARACABEY":"9341","KELES":"9342","KESTEL":"17893","MUDANYA":"9343","MUSTAFA KEMALPASA":"9344","ORHANELI":"17894","ORHANGAZI":"9345","YENISEHIR":"9346"},"CANAKKALE":{"AYVACIK":"9347","BAYRAMIC":"9348","BIGA":"9349","BOZCAADA":"9350","CAN":"9351","CANAKKALE":"9352","EZINE":"17882","GELIBOLU":"9353","GOKCEADA":"9354","LAPSEKI":"9355","YENICE":"9356"},"CANKIRI":{"ATKARACALAR":"9357","BAYRAMOREN":"9358","CANKIRI":"9359","CERKES":"9360","ILGAZ":"9361","KIZILIRMAK":"9362","KURSUNLU":"9363","ORTA":"9364","SABANOZU":"9365","YAPRAKLI":"9366"},"CORUM":{"ALACA":"9367","BAYAT":"9368","BOGAZKALE":"9369","CORUM":"9370","DODURGA":"9371","ISKILIP":"9372","KARGI":"9373","LACIN":"9374","MECITOZU":"9375","OGUZLAR":"9376","ORTAKOY":"9377","OSMANCIK":"9378","SUNGURLU":"9379","UGURLUDAG":"9380"},"DENIZLI":{"ACIPAYAM":"19020","BABADAG":"9382","BAKLAN":"9383","BEKILLI":"9384","BEYAGAC":"9385","BOZKURT":"9386","BULDAN":"9387","CAL":"9388","CAMELI":"9389","CARDAK":"9390","CIVRIL":"9391","DENIZLI":"9392","GUNEY":"9381","HONAZ":"9393","KALE":"17899","SARAYKOY":"9395","SERINHISAR":"9396","TAVAS":"17900"},"DIYARBAKIR":{"BISMIL":"9397","CERMIK":"9398","CINAR":"9399","CUNGUS":"9400","DICLE":"9401","DIYARBAKIR":"9402","EGIL":"9403","ERGANI":"9404","HANI":"9405","HAZRO":"9406","KOCAKOY":"9407","KULP":"9408","LICE":"9409","SILVAN":"9410"},"DUZCE":{"AKCAKOCA":"9411","CILIMLI":"9412","CUMAYERI":"9413","DUZCE":"9414","GOLYAKA":"9415","GUMUSOVA":"9416","KAYNASLI":"9417","YIGILCA":"9418"},"EDIRNE":{"EDIRNE":"9419","ENEZ":"9420","HAVSA":"9421","IPSALA":"9422","KESAN":"9423","LALAPASA":"9424","MERIC":"9425","SULOGLU":"9426","UZUNKOPRU":"9427"},"ELAZIG":{"AGIN":"9428","ALACAKAYA":"9429","ARICAK":"9430","BASKIL":"9431","ELAZIG":"9432","KARAKOCAN":"9433","KEBAN":"9434","KOVANCILAR":"9435","MADEN":"9436","PALU":"9437","SIVRICE":"9438"},"ERZINCAN":{"CAYIRLI":"9439","ERZINCAN":"9440","ILIC":"9441","KEMAH":"9442","KEMALIYE":"9443","OTLUKBELI":"9444","REFAHIYE":"9445","TERCAN":"9446","UZUMLU":"9447"},"ERZURUM":{"ASKALE":"9448","AZIZIYE":"9449","CAT":"9450","ERZURUM":"9451","HINIS":"9452","HORASAN":"9453","ISPIR":"9454","KARACOBAN":"9455","KARAYAZI":"9456","KOPRUKOY":"9457","NARMAN":"9458","OLTU":"9459","OLUR":"9460","PASINLER":"9461","PAZARYOLU":"9462","SENKAYA":"9463","TEKMAN":"9464","TORTUM":"9465","UZUNDERE":"9466"},"ESKISEHIR":{"ALPU":"9467","BEYLIKOVA":"9468","CIFTELER":"9469","ESKISEHIR":"9470","GUNYUZU":"9471","HAN":"9472","INONU":"9473","MAHMUDIYE":"9474","MIHALICCIK":"9475","SARICAKAYA":"17919","SEYITGAZI":"9476","SIVRIHISAR":"9477"},"GAZIANTEP":{"ARABAN":"9478","GAZIANTEP":"9479","ISLAHIYE":"9480","KARKAMIS":"9481","NIZIP":"9482","NURDAGI":"9483","OGUZELI":"9484","YAVUZELI":"9485"},"GIRESUN":{"ALUCRA":"9486","BULANCAK":"9487","CAMOLUK":"9488","CANAKCI":"9489","DERELI":"9490","DOGANKENT":"9491","ESPIYE":"9492","EYNESIL":"9493","GIRESUN":"9494","GORELE":"9495","GUCE":"9496","KESAP":"9497","PIRAZIZ":"9498","SEBINKARAHISAR":"16706","TIREBOLU":"9499","YAGLIDERE":"9500"},"GUMUSHANE":{"GUMUSHANE":"9501","KELKIT":"16746","KOSE":"9502","KURTUN":"9503","SIRAN":"9504","TORUL":"9505"},"HAKKARI":{"CUKURCA":"9506","DERECIK":"20067","HAKKARI":"9507","SEMDINLI":"9508","YUKSEKOVA":"9509"},"HATAY":{"ALTINOZU":"9510","ARSUZ":"9515","BELEN":"9511","DORTYOL":"9512","ERZIN":"9513","HASSA":"9514","HATAY":"20089","ISKENDERUN":"9516","KIRIKHAN":"9517","KUMLU":"9518","PAYAS":"17810","REYHANLI":"9519","SAMANDAG":"9520","YAYLADAG":"16730"},"IGDIR":{"ARALIK":"9521","IGDIR":"9522","KARAKOYUNLU":"9523","TUZLUCA":"9524"},"ISPARTA":{"AKSU (I)":"9525","ATABEY":"17891","EGIRDIR":"9526","GELENDOST":"9527","GONEN":"17892","ISPARTA":"9528","KECIBORLU":"9529","SARKI KARAAGAC":"9530","SENIRKENT":"17816","SUTCULER":"9531","ULUBORLU":"9532","YALVAC":"9533","YENISAR BADEMLI":"9534"},"ISTANBUL":{"ARNAVUTKOY":"9535","AVCILAR":"17865","BASAKSEHIR":"17866","BEYLIKDUZU":"9536","BUYUKCEKMECE":"9537","CATALCA":"9538","CEKMEKOY":"9539","ESENYURT":"9540","ISTANBUL":"9541","KARTAL":"9542","KUCUKCEKMECE":"9543","MALTEPE":"9544","PENDIK":"9545","SANCAKTEPE":"9546","SILE":"9547","SILIVRI":"9548","SULTANBEYLI":"9549","SULTANGAZI":"9550","TUZLA":"9551"},"IZMIR":{"ALIAGA":"9552","BAYINDIR":"9553","BERGAMA":"9554","BEYDAG":"9555","CESME":"9556","DIKILI":"9557","FOCA":"9558","GUZELBAHCE":"9559","IZMIR":"9560","KARABURUN":"9561","KEMALPASA":"9562","KINIK":"9563","KIRAZ":"9564","MENDERES":"17868","MENEMEN":"17869","ODEMIS":"9565","SEFERIHISAR":"9566","SELCUK":"9567","TIRE":"9568","TORBALI":"9569","URLA":"9570"},"KAHRAMANMARAS":{"AFSIN":"9571","ANDIRIN":"9572","CAGLAYANCERIT":"9573","EKINOZU":"9574","ELBISTAN":"9575","GOKSUN":"9576","KAHRAMANMARAS":"9577","NURHAK":"9578","PAZARCIK":"9579","TURKOGLU":"17908"},"KARABUK":{"EFLANI":"9580","ESKIPAZAR":"17890","KARABUK":"9581","OVACIK (K)":"9582","YENICE (K)":"9583"},"KARAMAN":{"AYRANCI":"9584","BASYAYLA":"9585","ERMENEK":"9586","KARAMAN":"9587","KAZIMKARABEKIR":"9588","SARIVELILER":"9589"},"KARS":{"AKYAKA":"9590","ARPACAY":"9591","DIGOR":"9592","KAGIZMAN":"9593","KARS":"9594","SARIKAMIS":"9595","SELIM":"9596","SUSUZ":"17880"},"KASTAMONU":{"ABANA":"9597","AGLI":"9598","ARAC":"9599","AZDAVAY":"9600","BOZKURT (K)":"9601","CATALZEYTIN":"9602","CIDE":"9603","DADAY":"9604","DEVREKANI":"17885","DOGANYURT":"9605","HANONU":"9606","IHSANGAZI":"9607","INEBOLU":"9608","KASTAMONU":"9609","KURE":"9610","PINARBASI (K)":"9611","SENPAZAR":"9612","SEYDILER":"17886","TASKOPRU":"9613","TOSYA":"9614"},"KAYSERI":{"AKKISLA":"9615","BUNYAN":"9616","DEVELI":"9617","FELAHIYE":"9618","INCESU":"9619","KAYSERI":"9620","OZVATAN":"9621","PINARBASI":"9622","SARIOGLAN":"9623","SARIZ":"9624","TOMARZA":"9625","YAHYALI":"9626","YESILHISAR":"9627"},"KILIS":{"ELBEYLI":"9628","KILIS":"9629","MUSABEYLI":"9630","POLATELI":"17907"},"KIRIKKALE":{"BALISEYH":"9631","CELEBI":"9632","DELICE":"9633","KARAKECILI":"9634","KESKIN":"17897","KIRIKKALE":"9635","SULAKYURT":"9636"},"KIRKLARELI":{"BABAESKI":"17903","DEMIRKOY":"9637","KIRKLARELI":"9638","LULEBURGAZ":"9639","PEHLIVANKOY":"9640","PINARHISAR":"9641","VIZE":"9642"},"KIRSEHIR":{"AKCAKENT":"20039","AKPINAR":"9643","CICEKDAGI":"9644","KAMAN":"9645","KIRSEHIR":"9646","MUCUR":"9647"},"KOCAELI":{"CAYIROVA":"9648","DARICA":"9649","DILOVASI":"9650","GEBZE":"9651","KANDIRA":"9652","KARAMURSEL":"9653","KARTEPE":"17902","KOCAELI":"9654","KORFEZ":"9655"},"KONYA":{"AHIRLI":"9656","AKOREN":"9657","AKSEHIR":"9658","ALTINEKIN":"9659","BEYSEHIR":"9660","BOZKIR":"9661","CELTIK":"9662","CIHANBEYLI":"9663","CUMRA":"9664","DERBENT":"9665","DEREBUCAK":"9666","DOGANHISAR":"9667","EMIRGAZI":"9668","EREGLI":"9669","GUNEYSINIR":"9670","HADIM":"16704","HALKAPINAR":"9671","HUYUK":"9672","ILGIN":"9673","KADINHANI":"9674","KARAPINAR":"9675","KARATAY":"17872","KONYA":"9676","KULU":"9677","MERAM":"17870","SARAYONU":"17874","SELCUKLU":"17871","SEYDISEHIR":"9678","TASKENT":"17873","TUZLUKCU":"9679","YALIHUYUK":"9680","YUNAK":"9681"},"KUTAHYA":{"ALTINTAS":"9682","ASLANAPA":"9683","CAVDARHISAR":"9684","DOMANIC":"9685","DUMLUPINAR":"17906","EMET":"9686","GEDIZ":"9687","HISARCIK":"9688","KUTAHYA":"9689","PAZARLAR":"9690","SAPHANE":"9691","SIMAV":"9692","TAVSANLI":"9693"},"MALATYA":{"AKCADAG":"9694","ARAPGIR":"9695","ARGUVAN":"9696","DARENDE":"9697","DOGANSEHIR":"9698","DOGANYOL":"9699","HEKIMHAN":"9700","KALE (M)":"9701","KULUNCAK":"9702","MALATYA":"9703","PUTURGE":"9704","YAZIHAN":"9705","YESILYURT":"9706"},"MANISA":{"AHMETLI":"9707","AKHISAR":"9708","ALASEHIR":"9709","DEMIRCI":"9710","GOLMARMARA":"9711","GORDES":"9712","KIRKAGAC":"9713","KOPRUBASI":"9714","KULA":"9715","MANISA":"9716","SALIHLI":"9717","SARIGOL":"9718","SARUHANLI":"9719","SELENDI":"9720","SOMA":"9721","TURGUTLU":"9722"},"MARDIN":{"DARGECIT":"9723","DERIK":"9724","KIZILTEPE":"9725","MARDIN":"9726","MAZIDAGI":"9727","MIDYAT":"9728","NUSAYBIN":"9729","OMERLI":"9730","SAVUR":"17901"},"MERSIN":{"ANAMUR":"9731","AYDINCIK":"9732","BOZYAZI":"9733","CAMLIYAYLA":"9734","ERDEMLI":"9735","GULNAR":"9736","MERSIN":"9737","MUT":"9738","SILIFKE":"9739","TARSUS":"9740"},"MUGLA":{"BODRUM":"9741","DALAMAN":"9742","DATCA":"9743","FETHIYE":"9744","KOYCEGIZ":"9745","MARMARIS":"17883","MILAS":"9746","MUGLA":"9747","ORTACA":"9748","SEYDIKEMER":"17884","ULA":"9749","YATAGAN":"9750"},"MUS":{"BULANIK":"9751","HASKOY":"9752","KORKUT":"9753","MALAZGIRT":"9754","MUS":"9755","VARTO":"9756"},"NEVSEHIR":{"ACIGOL":"9757","AVANOS":"17878","HACIBEKTAS":"9758","KOZAKLI":"9759","NEVSEHIR":"9760","URGUP":"9761"},"NIGDE":{"ALTUNHISAR":"9762","BOR":"9763","CAMARDI":"9764","CIFTLIK":"9765","NIGDE":"9766","ULUKISLA":"9767"},"ORDU":{"AKKUS":"9768","AYBASTI":"9769","CAMAS":"9770","CATALPINAR":"9771","CAYBASI":"9772","FATSA":"9773","GOLKOY":"9774","GULYALI":"9775","GURGENTEPE":"9776","IKIZCE":"9777","KABATAS":"9778","KORGAN":"9779","KUMRU":"9780","MESUDIYE":"9781","ORDU":"9782","UNYE":"9783"},"OSMANIYE":{"BAHCE":"9784","DUZICI":"9785","HASANBEYLI":"9786","KADIRLI":"9787","OSMANIYE":"9788","SUMBAS":"9789","TOPRAKKALE":"9790"},"RIZE":{"ARDESEN":"9791","CAMLIHEMSIN":"9792","CAYELI":"9793","FINDIKLI":"9794","HEMSIN":"9795","IKIZDERE":"9796","IYIDERE":"9797","PAZAR":"9798","RIZE":"9799"},"SAKARYA":{"AKYAZI":"9800","GEYVE":"9801","HENDEK":"9802","KARASU":"9803","KAYNARCA":"9804","KOCAALI":"9805","PAMUKOVA":"9806","SAKARYA":"9807","TARAKLI":"9808"},"SAMSUN":{"19 MAYIS":"9809","ALACAM":"9810","ASARCIK":"9811","ATAKUM":"17911","AYVACIK (S)":"9812","BAFRA":"9813","CARSAMBA":"9814","HAVZA":"9815","KAVAK":"9816","LADIK":"9817","SALIPAZARI":"9818","SAMSUN":"9819","TEKKEKOY":"9820","TERME":"9821","VEZIRKOPRU":"9822","YAKAKENT":"9823"},"SANLIURFA":{"AKCAKALE":"9824","BIRECIK":"9825","BOZOVA":"9826","CEYLANPINAR":"9827","HALFETI":"9828","HARRAN":"9829","HILVAN":"9830","SANLIURFA":"9831","SIVEREK":"9832","SURUC":"9833","VIRANSEHIR":"9834"},"SIIRT":{"BAYKAN":"9835","ERUH":"9836","KURTALAN":"9837","PERVARI":"9838","SIIRT":"9839","SIRVAN":"17888"},"SINOP":{"AYANCIK":"9840","BOYABAT":"9841","DIKMEN":"9842","DURAGAN":"9843","ERFELEK":"9844","GERZE":"9845","SARAYDUZU":"9846","SINOP":"9847","TURKELI":"9848"},"SIRNAK":{"BEYTUSSEBAP":"9849","CIZRE":"9850","GUCLUKONAK":"9851","IDIL":"9852","SILOPI":"9853","SIRNAK":"9854","ULUDERE":"9855"},"SIVAS":{"AKINCILAR":"9856","ALTINYAYLA(S)":"9857","DIVRIGI":"9858","DOGANSAR":"9859","GEMEREK":"9860","GOLOVA":"9861","GURUN":"9862","HAFIK":"9863","IMRANLI":"9864","KANGAL":"9865","KOYULHISAR":"9866","SARKISLA":"9867","SIVAS":"9868","SUSEHRI":"9869","ULAS":"17920","YILDIZELI":"9870","ZARA":"9871"},"TEKIRDAG":{"CERKEZKOY":"9872","CORLU":"9873","ERGENE":"17904","HAYRABOLU":"9874","KAPAKLI":"17905","M.EREGLISI":"9875","MALKARA":"9876","SARAY":"9877","SARKOY":"9878","TEKIRDAG":"9879"},"TOKAT":{"ALMUS":"9880","ARTOVA":"9881","BASCIFTLIK":"9882","ERBAA":"17910","NIKSAR":"9883","PAZAR (T)":"9884","RESADIYE":"9885","SULUSARAY":"9886","TOKAT":"9887","TURHAL":"9888","YESILYURT":"9889","ZILE":"9890"},"TRABZON":{"AKCAABAT":"9891","ARAKLI":"9892","ARSIN":"9893","BESIKDUZU":"9894","CARSIBASI":"9895","CAYKARA":"9896","DERNEKPAZARI":"9897","DUZKOY":"9898","HAYRAT":"9899","KOPRUBASI (T)":"9900","OF":"9901","SALPAZARI":"9902","SURMENE":"9903","TONYA":"9904","TRABZON":"9905","VAKFIKEBIR":"9906","YOMRA":"9907"},"TUNCELI":{"CEMISGEZEK":"9908","HOZAT":"9909","NAZIMIYE":"9910","OVACIK":"9911","PERTEK":"9912","PULUMUR":"9913","TUNCELI":"9914"},"USAK":{"BANAZ":"9915","ESME":"9916","KARAHALLI":"9917","SIVASLI":"9918","USAK":"9919"},"VAN":{"BAHCESARAY":"9920","BASKALE":"9921","CALDIRAN":"9922","CATAK":"9923","EDREMIT (V)":"9924","ERCIS":"9925","GEVAS":"9926","GURPINAR":"17912","MURADIYE":"9927","OZALP":"9928","SARAY (V)":"9929","VAN":"9930"},"YALOVA":{"ALTINOVA":"9931","ARMUTLU":"9932","CINARCIK":"9933","TERMAL":"9934","YALOVA":"9935"},"YOZGAT":{"AKDAGMADENI":"9936","AYDINCIK (Y)":"9937","BOGAZLIYAN":"9938","CANDIR":"9939","CAYIRALAN":"9940","CEKEREK":"9941","KADISEHRI":"9942","SARAYKENT":"9943","SARIKAYA":"9944","SEFAATLI":"17879","SORGUN":"9946","YENIFAKILI":"9947","YERKOY":"9948","YOZGAT":"9949"},"ZONGULDAK":{"ALAPLI":"9950","CAYCUMA":"9951","DEVREK":"9952","GOKCEBEY":"9953","KARADENIZ EREGLI":"9954","ZONGULDAK":"9955"}} # nopep8

tz = pytz.timezone("Europe/Istanbul")

async def get_data(ilceid: str, ilce, message):
    bugun = datetime.now(tz).strftime("%d.%m.%Y")
    yarin = (datetime.now(tz) + timedelta(days=1)).strftime("%d.%m.%Y")
    response = requests.get(f"http://namazvakitleri.diyanet.gov.tr/tr-TR/{ilceid}/{ilce}-icin-namaz-vakti", headers=Hea)
    data = response.text
    response = data.split('<tbody>')[1].split('</tbody>')[0]
    resp_bugun = response.split('<tr>')[1].split('</tr>')[0]
    row_bugun = re.findall('<td>(.*?)</td>', resp_bugun)
    resp_yarin = response.split('<tr>')[2].split('</tr>')[0]
    row_yarin = re.findall('<td>(.*?)</td>', resp_yarin)
    return {'bugun': [row_bugun[1], row_bugun[5]], 'yarin': [row_yarin[1], row_yarin[5]]}



@Client.on_message(filters.command('iftar')) 
async def iftar(bot, message):
    try:
        tmp = unidecode(message.text).upper().split()
        if len(tmp) < 2:
            await message.reply_text("Hatalı Kullanım!\nDoğru Kullanım: `/iftar İstanbul Avcılar`")
            return
        if len(tmp) == 2:
            il = tmp[1]
            ilce = tmp[1]
        if len(tmp) > 2:
            il = tmp[1]
            ilce = tmp[2]
        if il in idjson:  # girilen il, il listemizde varsa
            if ilce in idjson[il]:  # girilen ilce, ilce listemizde varsa
                bugun_t = datetime.now(tz).timestamp()  # şu anın timestamp'i (utc+3)
                bugun = datetime.fromtimestamp(bugun_t, tz).strftime('%d.%m.%Y')
                vakitler = await get_data(idjson[il][ilce], ilce, message)
                await message.reply_text(vakitler)
                ezan_saat = vakitler['bugun'][2]  # bugünün ezan vakti
                ezan_t = datetime.strptime(f'{ezan_saat} {bugun} +0300', '%H:%M %d.%m.%Y %z').timestamp()  # bugünkü ezan saatinin timestamp'i
                if ezan_t < bugun_t:  # ezan vakti geçmişse
                    tmp_t = bugun_t + 24*60*60  # bir sonraki güne geçmek için
                    yarin = datetime.fromtimestamp(tmp_t, tz).strftime('%d.%m.%Y')
                    ezan_saat = vakitler['yarin'][1]  # yarının ezan vakti
                    ezan_t = datetime.strptime(f'{ezan_saat} {yarin} +0300', '%H:%M %d.%m.%Y %z').timestamp()  # yarınki ezan saatinin timestamp'i
                kalan = ezan_t - bugun_t  # kalan süreyi hesaplayalım
                h = int(kalan / 3600)  # kalan saat
                m = int((kalan % 3600) / 60)  # kalan dakika
                _kalan = f'{h} saat, {m} dakika'
                mesaj = f'{ilce} için **{ezan_saat}** saatine kadar aç kalmalısın 🤤...\n**{_kalan}** daha dayanmalısın...'
                await message.reply_text(mesaj)
            else:
                await message.reply_text("İstediğin Yerde Ezanın Kaçta Okunduğunu Bilmiyorum :/") 
        else:
            await message.reply_text("İstediğin Yerde Ezanın Kaçta Okunduğunu Bilmiyorum :/") 
    except Exception as e:
        await message.reply_text(e)

@Client.on_message(filters.command('sahur')) 
async def sahur(bot, message):
    try:
        tmp = unidecode(message.text).upper().split()
        if len(tmp) < 2:
            await message.reply_text("Hatalı Kullanım!\nDoğru Kullanım: `/iftar İstanbul Avcılar`")
            return
        if len(tmp) == 2:
            il = tmp[1]
            ilce = tmp[1]
        if len(tmp) > 2:
            il = tmp[1]
            ilce = tmp[2]
        if il in idjson:  # girilen il, il listemizde varsa
            if ilce in idjson[il]:  # girilen ilce, ilce listemizde varsa
                bugun_t = datetime.now(tz).timestamp()  # şu anın timestamp'i (utc+3)
                bugun = datetime.fromtimestamp(bugun_t, tz).strftime('%d.%m.%Y')
                vakitler = await get_data(idjson[il][ilce], ilce, message)
                ezan_saat = vakitler['bugun'][1]  # bugünün ezan vakti
                ezan_t = datetime.strptime(f'{ezan_saat} {bugun} +0300', '%H:%M %d.%m.%Y %z').timestamp()  # bugünkü ezan saatinin timestamp'i
                if ezan_t < bugun_t:  # ezan vakti geçmişse
                    tmp_t = bugun_t + 24*60*60  # bir sonraki güne geçmek için
                    yarin = datetime.fromtimestamp(tmp_t, tz).strftime('%d.%m.%Y')
                    ezan_saat = vakitler['yarin'][0]  # yarının ezan vakti
                    ezan_t = datetime.strptime(f'{ezan_saat} {yarin} +0300', '%H:%M %d.%m.%Y %z').timestamp()  # yarınki ezan saatinin timestamp'i
                kalan = ezan_t - bugun_t  # kalan süreyi hesaplayalım
                h = int(kalan / 3600)  # kalan saat
                m = int((kalan % 3600) / 60)  # kalan dakika
                _kalan = f'{h} saat, {m} dakika'
                mesaj = f'{ilce} için Sıradaki Sahur Saati: **{ezan_saat}**\nSıradaki Sahura Kalan Süre: **{_kalan}**'
                await message.reply_text(mesaj)
            else:
                await message.reply_text("İstediğin Yerde Ezanın Kaçta Okunduğunu Bilmiyorum :/") 
        else:
            await message.reply_text("İstediğin Yerde Ezanın Kaçta Okunduğunu Bilmiyorum :/") 
    except Exception as e:
        await message.reply_text(e)


@Client.on_message(filters.command('log'))
async def log_handler(bot, message):
    with open('log.txt', 'rb') as f:
        try:
            await bot.send_document(document=f,
                                  file_name=f.name, reply_to_message_id=message.id,
                                  chat_id=message.chat.id, caption=f.name)
        except Exception as e:
            await message.reply_text(str(e))
