"""
Plot the model selection of the VB-NMTF algorithm on the Sanger dataset.

We run our method on the entire random dataset, so no test set.

We plot the MSE, BIC and AIC.
"""

import numpy, matplotlib.pyplot as plt
from scipy.interpolate import Rbf

# Values grid search
vb_grid_all_values = {'MSE': [3.0272042557829102, 3.027204313772129, 3.0272043015013632, 3.0272042467532212, 3.0272043152289179, 3.0272043457836597, 3.0272043418876171, 3.0272044191011442, 3.027204313276306, 3.0272042389545017, 3.027205717446904, 2.5928259798539472, 2.5915536886183648, 2.5914928971016273, 2.6150791700078395, 2.5973910185759004, 2.6181799991889623, 2.6216407891101539, 2.6182052841606183, 2.6233327724172004, 3.0272057168232718, 2.592303920421593, 2.6169873269127635, 2.3754306005031851, 2.408351831046371, 2.3620942494575998, 2.3738604557116658, 2.3783274961230529, 2.3895340576738318, 2.3671228153601152, 3.0272081910219866, 2.5917201172499564, 2.3886393874645862, 2.1704584329641254, 2.1998722405263216, 2.386553892711897, 2.1864797363636805, 2.1892318273289773, 2.3716858378153964, 2.1772483439927046, 3.0272082062874786, 2.6010413752637085, 2.3592180130924878, 2.4072659935526945, 2.1932019937150957, 2.0577306581712125, 2.046493196318568, 2.0492453750067736, 2.3673561326014427, 2.3996005342336511, 3.0272117525952917, 2.5918350091439564, 2.3592204574089592, 2.1816113053143433, 2.2111782436508371, 2.3814579620509351, 2.4215489076953594, 2.4030005558215128, 2.3713006143765605, 2.6217883451839303, 3.0272082042854143, 2.5919539363618678, 2.4239322493910147, 2.3681043748239983, 2.0982515533554214, 2.6235990939111327, 2.3650413644166273, 2.1919770023715683, 2.6223587246840077, 2.6217315349460222, 3.0272042608797798, 2.5920039556611556, 2.3589723600106196, 2.1774945937681429, 2.5927569156991157, 2.1921323412725959, 2.4194956032092674, 2.2077675669408592, 2.4099521822659269, 2.6213730512972968, 3.0272120976887908, 2.5917287927594534, 2.3683747670398825, 2.1868268548701422, 2.2509939255013851, 2.3644541832455861, 2.2004692246745385, 2.194656793143174, 2.3690875663909359, 2.1845045915517214, 3.0272082041584571, 2.5919892510116309, 2.3908994385725548, 2.1853589449692641, 2.3592885820120664, 2.3572223535037065, 2.6218551864155293, 2.20758544762404, 2.3700487285802523, 2.6206652524051135], 'loglikelihood': [-138379.73431469389, -138380.5738743383, -138380.58028545143, -138379.75072691264, -138380.59357736367, -138383.96315792541, -138382.70862510122, -138382.71835832161, -138381.60176589293, -138379.78384135049, -138384.5879775848, -132953.72263577435, -132938.14378582552, -132937.34439621944, -133253.1548281259, -133022.02019984587, -133299.80764371829, -133348.17710103374, -133298.38344365891, -133368.79610786145, -138384.5982781011, -132955.03982370484, -133280.31121151993, -129889.0947625307, -130379.96086628054, -129702.84686129019, -129869.61467254325, -129945.43583818071, -130111.53424830781, -129778.79573059475, -138392.34951646748, -132958.47373654009, -130086.08135958182, -126741.53573148482, -127213.48171467663, -130062.60448951431, -127003.15243548976, -127053.90426764014, -129847.6566280947, -126863.99122675485, -138392.37845130221, -133063.81541056844, -129652.95518229487, -130360.85320132811, -127107.52797869523, -124889.22931893577, -124696.15495959821, -124751.74805338231, -129784.24651057005, -130260.96980433611, -138403.07094437382, -132960.13627758514, -129651.25976050772, -126919.32279377367, -127394.56717029482, -129988.95819020271, -130577.32379484238, -130309.43682358752, -129839.01580474584, -133348.72564778719, -138392.40534443909, -132950.44698257331, -130601.05526009417, -129786.54274512359, -125568.45365066166, -133374.63092272906, -129744.87583339697, -127098.19469576198, -133358.41599791282, -133350.12311095235, -138379.77535159816, -132951.1666869591, -129647.9313451483, -126856.43590107805, -132958.55352898262, -127093.31472586066, -130547.48493647401, -127346.03860729581, -130406.60204227155, -133343.45677150233, -138403.15717893731, -132947.48788688189, -129787.73978723458, -127005.06472355497, -128019.77571311966, -129736.34664820883, -127224.47533929429, -127140.54703411472, -129807.77936322009, -126987.22707805879, -138392.45967155055, -132942.5941175461, -130119.04361825192, -126980.12176673966, -129657.63755417173, -129629.78080623729, -133347.84930555624, -127337.13600028346, -129824.85207547544, -133334.29102951247], 'AIC': [278283.46862938779, 278565.14774867659, 278845.16057090287, 279123.50145382527, 279405.18715472735, 279691.92631585081, 279969.41725020244, 280249.43671664322, 280527.20353178587, 280803.56768270099, 279539.1759551696, 268959.4452715487, 269210.28757165105, 269490.68879243889, 270404.3096562518, 270224.04039969173, 271061.61528743658, 271440.35420206748, 271622.76688731782, 272045.59221572289, 280785.19655620219, 270210.07964740967, 271144.62242303987, 264646.1895250614, 265911.92173256108, 264841.69372258038, 265459.2293450865, 265894.87167636142, 266511.06849661563, 266129.5914611895, 282046.69903293496, 271464.94747308019, 266006.16271916364, 259603.07146296964, 260832.96342935326, 266817.20897902863, 260984.30487097951, 261371.80853528029, 267245.3132561894, 261563.9824535097, 283292.75690260442, 272923.63082113687, 266389.91036458977, 268093.70640265621, 261875.05595739046, 257726.45863787155, 257628.30991919641, 258027.49610676462, 268380.49302114011, 269621.93960867223, 284560.14188874763, 273964.27255517029, 267636.51952101546, 262462.64558754733, 263703.13434058963, 269181.91638040543, 270648.64758968476, 270402.87364717503, 269752.03160949168, 277061.45129557437, 285784.81068887818, 275192.89396514662, 270786.11052018835, 269449.08549024718, 261304.90730132331, 277209.26184545812, 270241.75166679395, 265240.38939152396, 278052.83199582563, 278328.2462219047, 287005.55070319632, 276442.3333739182, 270129.86269029661, 264840.87180215609, 277339.10705796524, 265902.62945172132, 273104.96987294802, 266996.07721459161, 273411.2040845431, 279578.91354300466, 288298.31435787462, 277682.97577376378, 271659.47957446915, 266390.12944710994, 268715.55142623931, 272444.69329641765, 267716.95067858859, 267845.09406822943, 273475.55872644018, 268130.45415611757, 289522.91934310109, 278921.18823509221, 273572.08723650384, 267592.24353347928, 273245.27510834346, 273487.56161247462, 281221.69861111249, 269498.27200056694, 274771.70415095089, 282088.58205902495], 'BIC': [285262.09745914891, 286825.93935555918, 288388.11495490692, 289948.6186149508, 291512.46709297434, 293081.36903121928, 294641.02274269238, 296203.20498625463, 297763.13457851874, 299321.66150655533, 292223.42914312129, 282935.01954217273, 284477.18292494741, 286048.90522840759, 288253.84717489284, 289364.89900100511, 291493.79497142229, 293163.85496872553, 294637.58873664821, 296351.73514772562, 299175.0741023444, 289900.43658177508, 292135.45874562848, 286937.50523587322, 289503.7168315961, 289733.96820983861, 291651.98322056793, 293388.10494006606, 295304.78114854346, 296223.78350134054, 306142.20093726768, 296870.08707118698, 292720.9400110445, 287627.48644862458, 290167.01610878226, 297460.8993522317, 292937.63293795666, 294634.77429603151, 301817.91671071469, 297446.22360180906, 313093.88316512771, 304043.5530829851, 298828.62862576288, 301851.22066315432, 296951.36621721351, 294121.56489701953, 295342.21217766934, 297060.19436456246, 308731.98727826291, 311292.22986511997, 320066.89250946144, 310798.9774807599, 305799.17875148088, 301953.25912288856, 304521.70218080666, 311328.43852549826, 314123.1240396534, 315205.30440201948, 315882.41666921193, 324519.79066017043, 326997.18566778256, 317742.38155447762, 314672.71071994607, 314672.79830043158, 307865.73272193433, 325107.19987649587, 319476.80230825837, 315812.55264341505, 329962.1078581434, 331574.63469464914, 333923.55004029121, 324706.60362699063, 319740.40385934658, 315797.68388718361, 329642.1900589703, 319551.98336870392, 328100.59470590815, 323337.97296352929, 331099.37074945832, 338613.35112389742, 340921.93805316003, 331662.0286905776, 326993.96171281138, 323080.04080698057, 326760.89200763835, 331845.4630993451, 328473.14970304444, 329956.72231421375, 336942.61619395285, 332952.94084515865, 347852.16739657708, 338615.02381564747, 334630.51034413837, 330015.25416819309, 337032.87327013654, 338639.74730134691, 347738.47182706412, 337379.63274359779, 344017.65242106107, 352699.11785621441]} 
values_K=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
values_L=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Values greedy search
vb_greedy_all_values = {'MSE': [3.0272042551947203, 3.027204256305112, 3.0272042923576148, 2.5914654932112464, 2.5918836849320201, 2.5914602381010914, 2.3493739958858635, 2.3511225674996381, 2.3584324978814539, 2.1868222893761833, 2.1911559705091568, 2.2016668628098452, 2.0510257720785683, 2.0546897432717603, 2.0586496735360251, 2.0826309185454925], 'loglikelihood': [-138379.73430838491, -138379.74014614287, -138380.57362950334, -132935.31284836732, -132949.35927074254, -132936.87960196467, -129506.33023969264, -129543.6258747291, -129641.90589727147, -127005.00858615834, -127072.80234078577, -127243.67779180428, -124768.25065830135, -124835.58530247367, -124903.988439383, -125310.14633691005], 'AIC': [278283.46861676982, 279529.48029228573, 278565.14725900668, 268922.62569673464, 270198.71854148508, 269207.75920392934, 263596.66047938529, 264921.2517494582, 264151.81179454294, 260130.01717231667, 261517.60468157154, 260893.35558360856, 257196.50131660269, 258585.17060494734, 257755.976878766, 259824.29267382011], 'BIC': [285262.09744653094, 292213.73348023742, 286825.93886588927, 282898.19996735867, 289889.07547585049, 284474.6545572257, 284587.4968019739, 291636.02904133906, 286443.12750535476, 288154.43215797161, 295275.11894206965, 290227.40826303756, 292272.81157642574, 299403.7384451644, 294151.08313791396, 301970.81481891294]} 
list_values_K=[1.0, 2.0, 1.0, 2.0, 3.0, 2.0, 3.0, 4.0, 3.0, 4.0, 5.0, 4.0, 5.0, 6.0, 5.0, 6.0] 
list_values_L=[1.0, 1.0, 2.0, 2.0, 2.0, 3.0, 3.0, 3.0, 4.0, 4.0, 4.0, 5.0, 5.0, 5.0, 6.0, 6.0]

metrics = ['AIC']#['BIC', 'AIC','MSE']

'''
""" First plot the grid search """
for metric in metrics:
    # Make three lists of indices X,Y,Z (K,L,metric)
    values = numpy.array(vb_grid_all_values[metric]).flatten()
    list_values_K = numpy.array([values_K for l in range(0,len(values_L))]).T.flatten()
    list_values_L = numpy.array([values_L for k in range(0,len(values_K))]).flatten()
    
    # Set up a regular grid of interpolation points
    Ki, Li = (numpy.linspace(min(list_values_K), max(list_values_K), 100), 
              numpy.linspace(min(list_values_L), max(list_values_L), 100))
    Ki, Li = numpy.meshgrid(Ki, Li)
    
    # Interpolate
    rbf = Rbf(list_values_K, list_values_L, values, function='linear')
    values_i = rbf(Ki, Li)
    
    # Plot
    plt.figure()
    plt.imshow(values_i, cmap='jet_r',
               vmin=min(values), vmax=max(values), origin='lower',
               extent=[min(values_K), max(values_K), min(values_L), max(values_L)])
    plt.scatter(list_values_K, list_values_L, c=values, cmap='jet_r', s=50)
    plt.colorbar()
    #plt.title("Grid Search VB %s" % metric)   
    plt.xlabel("K", fontsize=16)     
    plt.ylabel("L", fontsize=16)  
    plt.show()
    
    # Print the best value
    index, row_length = numpy.argmin(values), len(values_L)
    best_K,best_L = (values_K[index / row_length], values_L[index % row_length])
    print "Best K,L for metric %s: %s,%s." % (metric,best_K,best_L)
'''

    
""" Then plot the greedy search """
for metric in metrics:
    # Make three lists of indices X,Y,Z (K,L,metric)
    values = vb_greedy_all_values[metric]
    
    # Set up a regular grid of interpolation points
    Ki, Li = (numpy.linspace(min(values_K), max(values_K), 100), 
              numpy.linspace(min(values_L), max(values_L), 100))
    Ki, Li = numpy.meshgrid(Ki, Li)
    
    # Interpolate
    rbf = Rbf(list_values_K, list_values_L, values, function='multiquadric')
    values_i = rbf(Ki, Li)
    
    # Plot
    fig = plt.figure(figsize=(1.9,1.42))
    fig.subplots_adjust(left=0.07, right=0.90, bottom=0.18, top=0.98)
    plt.xlabel("K", fontsize=8, labelpad=0)
    plt.ylabel("L", fontsize=8, labelpad=-3)
    plt.yticks(fontsize=8)
    plt.xticks(fontsize=8)    
    
    vmin = min(values)
    vmax = max(values)#(2*min(values)+max(values))/3.
    plt.imshow(values_i, cmap='jet_r',
               vmin=vmin, vmax=vmax, origin='lower',
               extent=[min(values_K)-1, max(values_K)+1, min(values_L)-1, max(values_L)+1])
    plt.scatter(list_values_K, list_values_L, c=values, cmap='jet_r', s=5, vmin=vmin, vmax=vmax)
    cb = plt.colorbar()
    cb.ax.tick_params(labelsize=6)
    plt.show()
        
    plt.savefig("../graphs_Sanger/aic_Sanger_greedy_model_selection.png", dpi=600)
#'''