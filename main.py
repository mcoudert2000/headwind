import branca.colormap as cm
import matplotlib
import polyline
import folium
import math



# convert lat long coordinates to forward azimuth
# takes two points and finds angle in degrees between them 
def get_ratio(lat_lon, wind_direc):
    if(len(lat_lon) <= 1):
        return []
    i = 1
    ratio = []
    while(True):
        first = lat_lon[i-1]
        second = lat_lon[i]
        y = math.sin(first[1]-second[1]) * math.cos(second[0])
        x = math.cos(first[0])*math.sin(second[0]) - math.sin(first[0])*math.cos(second[0])*math.cos(first[1]-second[1])
        r = math.atan2(y, x)
        deg = (r*180/math.pi + 360) % 360
        diff = wind_direc - deg
        ratio.append(abs(diff))
        i += 1
        if(i == len(lat_lon)):
            return ratio

# OPTION 1
# customisable colors for certain angles
# def get_color(val):
#     valitudes = {
#         0: '#FF00FF', # red 
#         45: '#CC00FF', # darker red
#         90: '#9999FF', # grey
#         135: '#99CCFF', # dark green
#         180: '#00CCCC', # green
#         225: '#99CCFF', # dark green 
#         270: '#9999FF', # grey
#         315: '#CC00FF', # darker red
#         360: '#FF00FF', # red
#     }
#     first = -1
#     for valitude in valitudes.keys():
#         if first < val <= valitude:
#             return valitudes[valitude]
#         first = valitude
#     return '#00CCCC'

# def add_to_map(lat_lon, ratio, world_map):
#     j = 0
#     for k in range(len(lat_lon)-1):
#         color = get_color(ratio[j])
#         j += 1
#         line = folium.ColorLine([lat_lon[k], lat_lon[k+1]], colors=[1], colormap=[color,color], weight=2)
#         line.add_to(world_map)






# OPTION 2
def add_to_map(lat_lon, ratio, world_map): 
    minima = min(ratio)
    maxima = max(ratio)
    test = cm.LinearColormap(['red','green'], vmin=minima, vmax=maxima)
    colorline = folium.ColorLine(lat_lon, ratio, colormap = test, nb_steps=len(lat_lon), weight = 4, opacity=1)
    world_map.add_child(colorline)


# calling Map() function
world_map = folium.Map()
filepath = 'C:\\Users\\csoba\\Documents\\coding\\personal\\headwind\\headwind\\test.html'
# lat_lon = polyline.decode('{nccIj{`EnIuBdAo@b@g@b@y@To@l@cCf@{BLqA@kClAqRF_@Vk@VSRC`Ij@|QfAj@?TMJKnEcKpAiCbCoF~BoFt@yB`BmFjBkFh@eAb@q@h@e@n@_@h@]RUj@}@h@qA\\mAVwA`A{ExBaJvDaKrAqCzA_C|BcEfDyHf@mBr@cEb@kBj@}Bp@uB`FfEh@^nBd@`AF`Bo@d@KxBVZGbEqHhB}ErAaEjBaDd@q@~@y@tAy@l@ORARIZWhAcAo@zGfAPgAQn@{Gf@yCy@]s@o@o@m@mB{Ac@e@k@u@gAkAmBiCkGoHABCBEAAG?IBEB?Fa@tAmDdAqCX{@Zq@dB{E~AcE`C{FfDoIdBiEp@cC|@mCl@cB~@}BaCqCgAiASMq@SMIKMIOIg@OuBW{INmKAgAGy@McASw@}A{Dq@eBSs@Q_AKmAIyACeDLoPQgHFaE^oKZ}DfA}IVaCDw@AcBEo@Ki@k@iBGe@Es@CyEAqECaEJoC~@yIRcFHgEMyHOyFUoEWaHI}@UsAc@qA[o@[a@MQiB{Ac@_@aB{AYe@CODm@Nq@VcAJe@DcAF_BBmGDaC@_BGwAOcCSqA]}@_C}DqA_CiAeCaA}B}@}BSs@Oy@WuCEwA@mAJeGAy@OiAS}@Yo@gD}FaH{LyEyHy@yA_AuBWs@c@sBYqBIgAIkBOeIWaHM}ASa@MQH[dCiIl@oBhEuLfEkL~AeEn@sA~BuE~BuE~@qBp@}Bd@yB`@wCTyCF_B@gEE{BU}CUmBg@sC[_BW}@]y@qB_E{A{B{@kAk@s@[WcC}AmA{@gBgBkPmRsDiE}BiDQQ]U{C{AU[EKE]?s@L_Ar@iDZaC`AiGLqABs@?yDDmBFQFEXCt@ApC[jBOjABfCR\\?PEPKVYXo@bBsGbDiJX}@l@iCr@qC|@uCZu@j@{@hCgDfHeIn@aA^q@v@kBRw@^cBt@uF|AmL^{CRgCHmBDoBCaEMoCQqBUeB[cB]{A[gA}@eC]cAMq@M}@GeBEiA@i@VkBBg@?m@EQCY@w@DYR[RMRARFTD\\ALGv@k@hBqA~BsAfGiDrCsBn@c@?AA??AAA?C@EBA@@@@?@XST[Rm@\\eAhA}DJ{@Ro@?IBQFGHCFBDH@FJH^f@^f@bFjJd@|@RVRDLEJI\\}@ZmAX_BL_AT_B`@kCj@iDF_@HONSVAL@D@TWj@o@`@_@dAyAVg@n@}A`BaFR_ATJtBx@HJXl@bD~AHaAFYXm@JkAFiA')
lat_lon = polyline.decode('zkrIm`inANPD?BDXGPKLATHNRBRFtAR~AFjAHl@D|ALtATj@HHJBL?`@EZ?NQ\\Y^MZURGJKR]RMXYh@QdAWf@[~@aAFGb@?j@YJKBU@m@FKZ[NSPKTCRJD?`@Wf@Wb@g@HCp@Qh@]z@SRMRE^EHJZnDHbBGPHb@NfBTxBN|DVbCBdA^lBFl@Lz@HbBDl@Lr@Bb@ApCAp@Ez@g@bEMl@g@`B_AvAq@l@    QF]Rs@Nq@CmAVKCK?_@Nw@h@UJIHOZa@xA]~@UfASn@U`@_@~@[d@Sn@s@rAs@dAGN?NVhAB\\Ox@@b@S|A?Tl@jBZpAt@vBJhATfGJn@b@fARp@H^Hx@ARGNSTIFWHe@AGBOTAP@^\\zBMpACjEWlEIrCKl@i@nAk@}@}@yBOWSg@kAgBUk@Mu@[mC?QLIEUAuAS_E?uCKyCA{BH{DDgF`AaEr@uAb@oA~@{AE}AKw@    g@qAU[_@w@[gAYm@]qAEa@FOXg@JGJ@j@o@bAy@NW?Qe@oCCc@SaBEOIIEQGaAe@kC_@{De@cE?KD[H[P]NcAJ_@DGd@Gh@UHI@Ua@}Bg@yBa@uDSo@i@UIICQUkCi@sCKe@]aAa@oBG{@G[CMOIKMQe@IIM@KB]Tg@Nw@^QL]NMPMn@@\\Lb@P~@XT')
# matching degrees means pure headwind
# opposite means pure tailwind
# for testing wind direction
test_direction = 180

ratio = get_ratio(lat_lon, test_direction)
add_to_map(lat_lon, ratio, world_map)

world_map.fit_bounds(world_map.get_bounds())
world_map.save(filepath)





# SCRAPPED CODE
# norm = matplotlib.colors.Normalize(vmin=minima, vmax=maxima, clip=True)
# test = []
# a = [] 
# j = 0
# for r in ratio:
#     color = cm.viridis(norm(r))
#     test.append(color)
#     a.append(j)
#     j += 1

# EXAMPLE CODE
# m = folium.Map([22.5, 22.5], zoom_start=3)
# color_line = folium.ColorLine(
#     [[0, 0], [0, 45], [45, 45], [45, 0], [0, 0]],
#     [0, 1, 2, 3],
#     colormap=['b', 'g', 'y', 'r'],
#     nb_steps=4,
#     weight=10,
#     opacity=1)
# m.add_child(color_line)
# m.save(filepath)