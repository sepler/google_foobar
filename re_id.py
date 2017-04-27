def answer(n):
    primes = "23571113171923293137414347535961677173798389971011031071091131271311371391491511571631671731791811911931971992112232272292332392412512572632692712772812832933073113133173313373473493533593673733793833893974014094194214314334394434494574614634674794874914995035095215235415475575635695715775875935996016076136176196316416436476536596616736776836917017097197277337397437517577617697737877978098118218238278298398538578598638778818838879079119199299379419479539679719779839919971009101310191021103110331039104910511061106310691087109110931097110311091117112311291151115311631171118111871193120112131217122312291231123712491259127712791283128912911297130113031307131913211327136113671373138113991409142314271429143314391447145114531459147114811483148714891493149915111523153115431549155315591567157115791583159716011607160916131619162116271637165716631667166916931697169917091721172317331741174717531759177717831787178918011811182318311847186118671871187318771879188919011907191319311933194919511973197919871993199719992003201120172027202920392053206320692081208320872089209921112113212921312137214121432153216121792203220722132221223722392243225122672269227322812287229322972309231123332339234123472351235723712377238123832389239323992411241724232437244124472459246724732477250325212531253925432549255125572579259125932609261726212633264726572659266326712677268326872689269326992707271127132719272927312741274927532767277727892791279728012803281928332837284328512857286128792887289729032909291729272939295329572963296929712999300130113019302330373041304930613067307930833089310931193121313731633167316931813187319132033209321732213229325132533257325932713299330133073313331933233329333133433347335933613371337333893391340734133433344934573461346334673469349134993511351735273529353335393541354735573559357135813583359336073613361736233631363736433659367136733677369136973701370937193727373337393761376737693779379337973803382138233833384738513853386338773881388939073911391739193923392939313943394739673989400140034007401340194021402740494051405740734079409140934099411141274129413341394153415741594177420142114217421942294231424142434253425942614271427342834289429743274337433943494357436343734391439744094421442344414447445144574463448144834493450745134517451945234547454945614567458345914597460346214637463946434649465146574663467346794691470347214723472947334751475947834787478947934799480148134817483148614871487748894903490949194931493349374943495149574967496949734987499349995003500950115021502350395051505950775081508750995101510751135119514751535167517151795189519752095227523152335237526152735279528152975303530953235333534753515381538753935399540754135417541954315437544154435449547154775479548355015503550755195521552755315557556355695573558155915623563956415647565156535657565956695683568956935701571157175737574157435749577957835791580158075813582158275839584358495851585758615867586958795881589759035923592759395953598159876007601160296037604360476053606760736079608960916101611361216131613361436151616361736197619962036211621762216229624762576263626962716277628762996301631163176323632963376343635363596361636763736379638963976421642764496451646964736481649165216529654765516553656365696571657765816599660766196637665366596661667366796689669167016703670967196733673767616763677967816791679368036823682768296833684168576863686968716883689969076911691769476949695969616967697169776983699169977001701370197027703970437057706970797103710971217127712971517159717771877193720772117213721972297237724372477253728372977307730973217331733373497351736973937411741774337451745774597477748174877489749975077517752375297537754175477549755975617573757775837589759176037607762176397643764976697673768176877691769977037717772377277741775377577759778977937817782378297841785378677873787778797883790179077919792779337937794979517963799380098011801780398053805980698081808780898093810181118117812381478161816781718179819182098219822182318233823782438263826982738287829182938297831183178329835383638369837783878389841984238429843184438447846184678501851385218527853785398543856385738581859785998609862386278629864186478663866986778681868986938699870787138719873187378741874787538761877987838803880788198821883188378839884988618863886788878893892389298933894189518963896989718999900190079011901390299041904390499059906790919103910991279133913791519157916191739181918791999203920992219227923992419257927792819283929393119319932393379341934393499371937793919397940394139419942194319433943794399461946394679473947994919497951195219533953995479551958796019613961996239629963196439649966196779679968996979719972197339739974397499767976997819787979198039811981798299833983998519857985998719883988799019907992399299931994199499967997310007100091003710039100611006710069100791009110093100991010310111101331013910141101511015910163101691017710181101931021110223102431024710253102591026710271102731028910301103031031310321103311033310337103431035710369103911039910427104291043310453104571045910463104771048710499105011051310529105311055910567105891059710601106071061310627106311063910651106571066310667106871069110709107111072310729107331073910753107711078110789107991083110837108471085310859108611086710883108891089110903109091093710939109491095710973109791098710993110031102711047110571105911069110711108311087110931111311117111191113111149111591116111171111731117711197112131123911243112511125711261112731127911287112991131111317113211132911351113531136911383113931139911411114231143711443114471146711471114831148911491114971150311519115271154911551115791158711593115971161711621116331165711677116811168911699117011171711719117311174311777117791178311789118011180711813118211182711831118331183911863118671188711897119031190911923119271193311939119411195311959119691197111981119871200712011120371204112043120491207112073120971210112107121091211312119121431214912157121611216312197122031221112227122391224112251122531226312269122771228112289123011232312329123431234712373123771237912391124011240912413124211243312437124511245712473124791248712491124971250312511125171252712539125411254712553125691257712583125891260112611126131261912637126411264712653126591267112689126971270312713127211273912743127571276312781127911279912809128211282312829128411285312889128931289912907129111291712919129231294112953129591296712973129791298313001130031300713009130331303713043130491306313093130991310313109131211312713147131511315913163131711317713183131871321713219132291324113249132591326713291132971330913313133271333113337133391336713381133971339913411134171342113441134511345713463134691347713487134991351313523135371355313567135771359113597136131361913627136331364913669136791368113687136911369313697137091371113721137231372913751137571375913763137811378913799138071382913831138411385913873138771387913883139011390313907139131392113931139331396313967139971399914009140111402914033140511405714071140811408314087141071414314149141531415914173141771419714207142211424314249142511428114293143031432114323143271434114347143691438714389144011440714411144191442314431144371444714449144611447914489145031451914533145371454314549145511455714561145631459114593146211462714629146331463914653146571466914683146991471314717147231473114737147411474714753147591476714771147791478314797148131482114827148311484314851148671486914879148871489114897149231492914939149471495114957149691498315013150171503115053150611507315077150831509115101151071512115131151371513915149151611517315187151931519915217152271523315241152591526315269152711527715287152891529915307153131531915329153311534915359153611537315377153831539115401154131542715439154431545115461154671547315493154971551115527155411555115559155691558115583156011560715619156291564115643156471564915661156671567115679156831572715731157331573715739157491576115767157731578715791157971580315809158171582315859158771588115887158891590115907159131591915923159371595915971159731599116001160071603316057160611606316067160691607316087160911609716103161111612716139161411618316187161891619316217162231622916231162491625316267162731630116319163331633916349163611636316369163811641116417164211642716433164471645116453164771648116487164931651916529165471655316561165671657316603166071661916631166331664916651166571666116673166911669316699167031672916741167471675916763167871681116823168291683116843168711687916883168891690116903169211692716931169371694316963169791698116987169931701117021170271702917033170411704717053170771709317099171071711717123171371715917167171831718917191172031720717209172311723917257172911729317299173171732117327173331734117351173591737717383173871738917393174011741717419174311744317449174671747117477174831748917491174971750917519175391755117569175731757917581175971759917609176231762717657176591766917681176831770717713177291773717747177491776117783177891779117807178271783717839178511786317881178911790317909179111792117923179291793917957179591797117977179811798717989180131804118043180471804918059180611807718089180971811918121181271813118133181431814918169181811819118199182111821718223182291823318251182531825718269182871828918301183071831118313183291834118353183671837118379183971840118413184271843318439184431845118457184611848118493185031851718521185231853918541185531858318587185931861718637186611867118679186911870118713187191873118743187491875718773187871879318797188031883918859188691889918911189131891718919189471895918973189791900119009190131903119037190511906919073190791908119087191211913919141191571916319181191831920719211192131921919231192371924919259192671927319289193011930919319193331937319379193811938719391194031941719421194231942719429194331944119447194571946319469194711947719483194891950119507195311954119543195531955919571195771958319597196031960919661196811968719697196991970919717197271973919751197531975919763197771979319801198131981919841198431985319861198671988919891199131991919927199371994919961199631997319979199911999319997200112002120023200292004720051200632007120089201012010720113201172012320129201432014720149201612017320177201832020120219202312023320249202612026920287202977"
    return primes[n] + primes[n+1] + primes[n+2] + primes[n+3] + primes[n+4]
