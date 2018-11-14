import os
execfile('wsadminlib.py')

def dockercreateJAAS(cfg):
    m = 'dockercreateJAAS:'
    sop(m,'ready:')
    auth_alias = "wassafety"
    auth_username = "wassafety"
    auth_password = "password"
    createJAAS(auth_alias, auth_username, auth_password)
    AdminConfig.save()
    sop(m,"Exit success.")

def dockerCreateStringNameSpaceBinding(cfg):
    m = 'dockerCreateStringNameSpaceBinding:'
    sop(m,'ready:')
    sop(m, 'cellName: '+cfg["cellName"])
    sop(m,'nodeName: '+ cfg["nodeName"])
    sop(m,'serverName: ' + cfg["serverName"])
    scope = cfg["serverID"]

    bindingName = 'TMO DWC3 - Demo'
    nameInNameSpace = 'tmo/param/dwcdemoclaim'
    stringToBind = '12345'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Documents - convert Doc URL'
    nameInNameSpace = 'tmo/param/convertDocGetPacketUrl'
    stringToBind = 'http://webdeint7/ConvertDoc/GetPacket'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Documents - doc list'
    nameInNameSpace = 'tmo/param/docList'
    stringToBind = 'ADDLINFO,AGTEND,AGTPOL,DECLINE,EMOD,INSPOL,POLICY,QUOTE,CNCLNTC,CNFNCOM,TXOSQTE,RNSTNTC,EXPIRCOM,FASTRACK,FINAUDIT,REJECT,ARGOENDT,ARGOPOL,AUDTOSC'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Documents - eiixdta'
    nameInNameSpace = 'tmo/db/schema/eiixdta'
    stringToBind = 'EIIDDTA'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Documents - eiixobj'
    nameInNameSpace = 'tmo/db/schema/eiixobj'
    stringToBind = 'EIIDOBJ'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO EOB - FairIssacUserId'
    nameInNameSpace = 'tmo/param/fairIssacUserId'
    stringToBind = '75DAAEC693'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO EOB - Redaction Date'
    nameInNameSpace = 'tmo/param/redactionDate'
    stringToBind = '3/1/2005'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO EOB -FairIssacPwd'
    nameInNameSpace = 'tmo/param/fairIssacPwd'
    stringToBind = 'BDA99081AA154D'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO EOB -FairIssacSite'
    nameInNameSpace = 'tmo/param/fairIssacSite'
    stringToBind = 'TMI'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO EOB -FairIssacURL'
    nameInNameSpace = 'tmo/param/fairIssacUrl'
    stringToBind = 'https://uat.mitchellsmartadvisor.com/XMLBill/STUB_GetXMLBill.asp'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Endorsements - IQ End Environment'
    nameInNameSpace = 'tmo/param/iqEndEnv'
    stringToBind = 'DEV'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Favor - favorHighSpeedPrinter'
    nameInNameSpace = 'tmo/param/favorHighSpeedPrinter'
    stringToBind = 'FAVOR'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Favor - favorPrinter'
    nameInNameSpace = 'tmo/param/favorPrinter'
    stringToBind = 'PAUIT03'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Favor - favorVolunteerClasscodes'
    nameInNameSpace = 'tmo/param/favorVolunteerClasscodes'
    stringToBind = '7720:014|7704:002'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Favor - loginPageTMO'
    nameInNameSpace = 'tmo/param/loginPageTMO'
    stringToBind = 'formslogin.aspx?reason'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO HotTopics - FileDirExt'
    nameInNameSpace = 'tmo/param/topicsDataFileDirExt'
    stringToBind = '\\aus-vmdev22\data\external'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO HotTopics - Hottopics FileDirIn'
    nameInNameSpace = 'tmo/param/topicsDataFileDirIn'
    stringToBind = '\\aus-vmdev22\data'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO HotTopics - topicsBaseURL'
    nameInNameSpace = 'tmo/param/topicsBaseURL'
    stringToBind = 'https://devcn.texasmutual.com/dynamicContentWeb/data/'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO LossRun - All Location Report'
    nameInNameSpace = 'tmo/param/allLocRptId'
    stringToBind = '12501'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO LossRun - Crystal Server'
    nameInNameSpace = 'tmo/param/tmoCrystalServer'
    stringToBind = 'AUS-VMDEV96'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    #   bindingName = 'TMO LossRun - Single Location Report'
#   stringToBind = '21151'
#   createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO OIR - BOA PaymentService URL'
    nameInNameSpace = 'tmo/param/TMOBoAPaymentServiceURL'
    stringToBind = 'http://aus-vmdev202:9797/intfBoAPayment-service.serviceagent/intfwsBoAPaymentEndpoint0'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO OIR - DataDir'
    nameInNameSpace = 'tmo/param/oirDataDir'
    stringToBind = '/QFileSvr.400/ASIA/TmiOIR/'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO OIR - Environment'
    nameInNameSpace = 'tmo/param/environment'
    stringToBind = 'DEV'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Payments - BoA Payment Service URL'
    nameInNameSpace = 'tmo/param/BoAPaymentServiceUrl'
    stringToBind = 'http://wdeonla/BoaCashProWeb/boaservice/makePayment'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Payments - Contract Agent Quote Window'
    nameInNameSpace = 'tmo/param/ContractAgentQuoteWindowDays'
    stringToBind = '3'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Payments - Installment Web Service URL'
    nameInNameSpace = 'tmo/param/installmentWebServiceUrl'
    stringToBind = 'http://webdeint/InstallmentsWeb/services/InstallmentDataWS'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Payments - Quote Payment Days Valid'
    nameInNameSpace = 'tmo/param/quotePaymentDaysValid'
    stringToBind = '59'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Payments - Requote Eligibility Service URL'
    nameInNameSpace = 'tmo/param/requoteEligibilityServiceUrl'
    stringToBind = 'http://devservice.texasmutual.com/IQIsRequoteEligible.aspx'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Safety - IMAGINGEMAIL'
    nameInNameSpace = 'tmo/param/osaLpImaging'
    stringToBind = 'mvuong@texasmutual.com'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Safety - TMOFAILUREEMAIL'
    nameInNameSpace = 'tmo/param/tmoFailureEmailRecipients'
    stringToBind = 'mvuong@texasmutual.com'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Safety - osaDataDir'
    nameInNameSpace = 'tmo/param/osaDataDir'
    stringToBind = '//ASIA/TmiSafetyQA$/'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Safety - osaDataNas'
    nameInNameSpace = 'tmo/param/osaDataNas'
    stringToBind = '//Asia/TmiHome$/safetyosa/'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO SelfAdmin - CorrespondenceService'
    nameInNameSpace = 'tmo/param/correspondenceServiceUrl'
    stringToBind = 'http://wdeint/ClientWeb/services/CorrespondenceService'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - Client xmlRpcJndiName'
    nameInNameSpace = 'tmo/param/clientxmlrpcurl'
    stringToBind = 'http://wdeint/clientService/xmlrpc'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - CommonUI Local Flag'
    nameInNameSpace = 'tmo/param/tmoCommonUILocalFlag'
    stringToBind = 'N'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - CompNow Deep Link URL'
    nameInNameSpace = 'tmo/param/compNowDeepLinkUrl'
    stringToBind = 'https://devcn.texasmutual.com/inituser.aspx'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - CompNow URL'
    nameInNameSpace = 'tmo/param/compNowUrl'
    stringToBind = 'https://devcn.texasmutual.com/'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - DAFI Service URL'
    nameInNameSpace = 'tmo/param/dafiServiceUrl'
    stringToBind = 'http://wdedocb/DAFIWeb2.0/DAFI'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - DafiServiceURL'
    nameInNameSpace = 'tmo/param/dafiservice-url'
    stringToBind = 'http://wdedocb/DAFIWeb2.0/DAFI'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - DafiwsdlDocumentURL'
    nameInNameSpace = 'tmo/param/dafiwsdl-url'
    stringToBind = 'http://wdedocb/DAFIWeb2.0/DAFI?WSDL'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - DocProcessingSvcUrlPrefix'
    nameInNameSpace = 'tmo/param/DocProcessingSvcUrlPrefix'
    stringToBind = 'http://aus-vmqa104.company.pvt'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - Public URL'
    nameInNameSpace = 'tmo/param/publicUrl'
    stringToBind = 'http://devwww.texasmutual.com/'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - Reload Script QueryString'
    nameInNameSpace = 'tmo/param/scriptquery'
    stringToBind = '?2015d'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - Session Cookie'
    nameInNameSpace = 'tmo/param/sessioncookie'
    stringToBind = 'TLTSID'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - TMO Environment'
    nameInNameSpace = 'tmo/param/tmoEnvironment'
    stringToBind = 'DEV'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - TMO Service URL'
    nameInNameSpace = 'tmo/param/tmoServiceUrl'
    stringToBind = 'http://devservice.texasmutual.com/'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - UCS Environment'
    nameInNameSpace = 'tmo/param/UCSEnv'
    stringToBind = 'DEV'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - ccixdta Schema'
    nameInNameSpace = 'tmo/db/schema/ccixdta'
    stringToBind = 'CCIDDTA'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - ccixobj Schema'
    nameInNameSpace = 'tmo/db/schema/ccixobj'
    stringToBind = 'CCIDOBJ'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - clnxdta Schema'
    nameInNameSpace = 'tmo/db/schema/clnxdta'
    stringToBind = 'CLNDDTA'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - fndcpdxdta Schema'
    nameInNameSpace = 'tmo/db/schema/fndcpxdtaSchema'
    stringToBind = 'FNDCPDDTA'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - fndcpxobj Schema'
    nameInNameSpace = 'tmo/db/schema/fndcpxobjSchema'
    stringToBind = 'FNDCPDOBJ'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - fndepxdta Schema'
    nameInNameSpace = 'tmo/db/schema/epaRdsrvrFndepxdtaSchema'
    stringToBind = 'FNDEPDDTA'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - fndepxobj Schema'
    nameInNameSpace = 'tmo/db/schema/epaRdsrvrPrgmSchema'
    stringToBind = 'FNDEPDOBJ'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - fndiuxdta Schema'
    nameInNameSpace = 'tmo/db/schema/fndiuxdtaSchema'
    stringToBind = 'ECDDTA'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - fndiuxobj Schema'
    nameInNameSpace = 'tmo/db/schema/fndiuxobjSchema'
    stringToBind = 'ECDOBJ'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - fndrpxdta'
    nameInNameSpace = 'tmo/db/schema/fndrpxdta'
    stringToBind = 'FNDRPPOBJ'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - fndrpxobj'
    nameInNameSpace = 'tmo/db/schema/fndrpxobj'
    stringToBind = 'FNDRPDOBJ'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - fnduwxdta Schema'
    nameInNameSpace = 'tmo/db/schema/fnduwxdta'
    stringToBind = 'FNDUWDGEN'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - fnduwxobj Schema'
    nameInNameSpace = 'tmo/db/schema/fnduwxobj'
    stringToBind = 'FNDUWDGEN'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - httpURLprefixDAFIOnlineApps'
    nameInNameSpace = 'tmo/param/httpURLprefixDAFIOnlineApps'
    stringToBind = 'http://wdedocb'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - httpURLprefixIntranetApps'
    nameInNameSpace = 'tmo/param/httpURLprefixIntranetApps'
    stringToBind = 'http://wdeint'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - httpURLprefixOnlineApps'
    nameInNameSpace = 'tmo/param/httpURLprefixOnlineApps'
    stringToBind = 'http://wdeonl'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - ieaxdta Schema'
    nameInNameSpace = 'tmo/db/schema/ieaxdta'
    stringToBind = 'IEADDTA'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - ieaxobj Schema'
    nameInNameSpace = 'tmo/db/schema/ieaxobj'
    stringToBind = 'IEADOBJ'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - inetxdta Schema'
    nameInNameSpace = 'tmo/db/schema/inetxdta'
    stringToBind = 'INETDEV'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - inetxobj Schema'
    nameInNameSpace = 'tmo/db/schema/inetxobj'
    stringToBind = 'INETDEV'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - premAuditAndSftyEmail'
    nameInNameSpace = 'tmo/param/premAuditAndSftyEmail'
    stringToBind = 'rxchaudh@texasmutual.com'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - publicSecureUrl'
    nameInNameSpace = 'tmo/param/publicSecureUrl'
    stringToBind = 'https://devwww.texasmutual.com/'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - refxdta' 
    nameInNameSpace = 'tmo/db/schema/refxdta'
    stringToBind = 'REFDDTA'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - tmoxdta Schema'
    nameInNameSpace = 'tmo/db/schema/tmoxdta'
    stringToBind = 'TMODDTA'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - tmoxobj Schema'
    nameInNameSpace = 'tmo/db/schema/tmoxobj'
    stringToBind = 'TMODOBJ'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared -CommonUiServ'
    nameInNameSpace = 'tmo/param/cmmnuiserv'
    stringToBind = 'webdeonl'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO TempUser - downloadAuditWebServiceUrl'
    nameInNameSpace = 'tmo/param/tempUserDownloadAuditWebServiceUrl'
    stringToBind = 'http://aus-vmdev65/EPAServiceSite_DEV/EPA.svc/basic'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'tmoLoginPage'
    nameInNameSpace = 'cell/legacyRoot/web/config/loginPageTMO'
    stringToBind = 'formslogin.aspx?reason'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'tmoxdtaSchema'
    nameInNameSpace = 'cell/persistent/schema/tmoxdtaSchema'
    stringToBind = 'TMODDTA'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'tmoxobjSchema'
    nameInNameSpace = 'cell/persistent/schema/tmoxobjSchema'
    stringToBind = 'TMODOBJ'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO BoA CashPro - Token Key'
    nameInNameSpace = 'tmo/param/tokenKey'
    stringToBind = 'TmI02012016oY38fQ19fEL46mb4c35'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO BoA CashPro - ClientID'
    nameInNameSpace = 'tmo/param/clientId'
    stringToBind = '700180001C'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - httpGwPolicyURLprefix'
    nameInNameSpace = 'tmo/param/httpGwPolicyURLprefix'
    stringToBind = 'http://gwdevpc'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - httpGwBillingURLprefix'
    nameInNameSpace = 'cell/persistent/tmo/param/httpGwBillingURLprefix'
    stringToBind = 'http://gwdevbc'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - Windows Intranet HTTP server'
    nameInNameSpace = 'tmo/param/httpWinURLprefixIntApps'
    stringToBind = 'http://wdeint'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - httpURLprefixOnlineWindowsApps'
    nameInNameSpace = 'tmo/param/httpURLprefixOnlineWindowsApps'
    stringToBind = 'http://wdeonl'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO BoA CashPro - URL Prefix'
    nameInNameSpace = 'tmo/param/cashProPrefix'
    stringToBind = 'https://api-cert.billingandpayments.com'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO BoA CashPro - Email Log'
    nameInNameSpace = 'tmo/param/cashProEmailLog'
    stringToBind = 'boacashpro@texasmutual.com'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - httpURLprefixFinApps'
    nameInNameSpace = 'tmo/param/httpURLprefixFinanceApps'
    stringToBind = 'http://wdefin'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - httpCdsURLprefix'
    nameInNameSpace = 'tmo/param/httpCdsURLprefix'
    stringToBind = 'http://wdeund'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - cdsxdta Schema'
    nameInNameSpace = 'tmo/db/schema/cdsxdta'
    stringToBind = 'CDSDDTA'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - Finance Environment'
    nameInNameSpace = 'tmo/param/financeEnvironment'
    stringToBind = 'PABSDEV'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'DAFI Service WSDL URL'
    nameInNameSpace = 'dafi/wsdl-url'
    stringToBind = 'http://wdedocb/DAFIWeb2.0/DAFI?WSDL'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'DAFI Service URL'
    nameInNameSpace = 'dafi/service-url'
    stringToBind = 'http://wdedocb/DAFIWeb2.0/DAFI'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - Billings Page'
    nameInNameSpace = 'tmo/param/billingsPage'
    stringToBind = 'eBizLiteWeb/#/composite;accountnum = '
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - httpURLprefixOnlineAppsWin'
    nameInNameSpace = 'tmo/param/httpURLprefixOnlineAppsWin'
    stringToBind = 'http://wdeonl'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - Windows Finance HTTP server'
    nameInNameSpace = 'tmo/param/httpWinURLprefixFinApps'
    stringToBind = 'http://wdefin'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Payments - Tibco Service URL'
    nameInNameSpace = 'tmo/param/paymentsTibcoURL'
    stringToBind = 'http://aus-vmdev202:32080/PaymentService'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO CompNow URL'
    nameInNameSpace = 'cell/legacyRoot/tmo/config/compNowUrl'
    stringToBind = 'https://devcn.texasmutual.com/'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO INET Data Schema'
    nameInNameSpace = 'cell/legacyRoot/tmo/config/schema/inet/data'
    stringToBind = 'INETDEV'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO INET Object Schema'
    nameInNameSpace = 'cell/legacyRoot/tmo/config/schema/inet/object'
    stringToBind = 'INETDEV'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Public URL'
    nameInNameSpace = 'cell/legacyRoot/tmo/config/publicUrl'
    stringToBind = 'http://devwww.texasmutual.com/'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO REFxDTA Schema'
    nameInNameSpace = 'cell/legacyRoot/tmo/config/REFxDTA'
    stringToBind = 'REFDDTA'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Service URL'
    nameInNameSpace = 'tmo/param/httpURLtmoservice'
    stringToBind = 'http://devservice.texasmutual.com/'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO UCS Environment Descriptor'
    nameInNameSpace = 'tmo/param/ucsEnvString'
    stringToBind = 'DEV'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'fnduwxdtaSchema'
    nameInNameSpace = 'cell/legacyRoot/db/config/dao/schema/fnduwxdtaSchema'
    stringToBind = 'FNDUWDGEN'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'fnduwxobjSchema'
    nameInNameSpace = 'cell/legacyRoot/db/config/dao/schema/fnduwxobjSchema'
    stringToBind = 'FNDUWDGEN'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'httpURLprefixIntranetApps'
    nameInNameSpace = 'cell/legacyRoot/param/httpURLprefixIntranetApps'
    stringToBind = 'http://wdeint'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'httpURLprefixOnlineApps'
    nameInNameSpace = 'cell/legacyRoot/param/httpURLprefixOnlineApps'
    stringToBind = 'http://webdeonl'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'ieaxdtaSchema'
    nameInNameSpace = 'cell/legacyRoot/db/config/dao/schema/ieaxdtaSchema'
    stringToBind = 'IEADDTA'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'ieaxobjSchema'
    nameInNameSpace = 'cell/legacyRoot/db/config/dao/schema/ieaxobjSchema'
    stringToBind = 'IEADOBJ'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - httpClaimCenterURLPrefix'
    nameInNameSpace = 'cell/persistent/tmo/param/httpClaimCenterUrlPrefix'
    stringToBind = 'http://gwdevcc'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - CDS Environment'
    nameInNameSpace = 'tmo/param/CDSEnv'
    stringToBind = 'DEV'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - cdsxobj'
    nameInNameSpace = 'tmo/db/schema/cdsxobj'
    stringToBind = 'CDSDOBJ'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - ecxobj Schema'
    nameInNameSpace = 'tmo/db/schema/ecxobj'
    stringToBind = 'ECDOBJ'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared -CoBrowseFlag'
    nameInNameSpace = 'tmo/param/cobrowseflag'
    stringToBind = 'Y'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'Shared - CompNow URL PABS'
    nameInNameSpace = 'tmo/param/compNowUrlPabs'
    stringToBind = 'https://devcn.texasmutual.com/'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO LDAP Server'
    nameInNameSpace = 'tmo/param/ldapServer'
    stringToBind = 'ldaps://aus-vmdc1.company.pvt:636'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - dwrxdta schema'
    nameInNameSpace = 'tmo/db/schema/dwrxdta'
    stringToBind = 'dwrddta'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - TXMPublicSecureUrl'
    nameInNameSpace = 'tmo/param/TXMPublicSecureUrl'
    stringToBind = 'https://qawww.texasmutual.com/'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'httpsPayGoUrlPrefix'
    nameInNameSpace = 'tmo/param/httpsPayGoUrlPrefix'
    stringToBind = 'https://texasmutual-paygo-functions-dev.azurewebsites.net'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'payGoCode'
    nameInNameSpace = 'tmo/param/payGoCode'
    stringToBind = '19ch0WrPgAY2fPxivNL5eL47Z8BbYSciGXIf3lKzH3OhNl0ihQXTvA=='
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'FinalAudit-Email Image Location'
    nameInNameSpace = 'tmo/param/finalAuditImageLoc'
    stringToBind = '\\\\aus-tmiappdata\\FormServices$\\Dev\\FORMSINPUT\\sourceData\\'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'Final Audit- Email Service Host'
    nameInNameSpace = 'tmo/param/finalAuditEmailServiceHost'
    stringToBind = 'http://AUS-VMDEV201:25550'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'claimsSQL'
    nameInNameSpace = 'cell/persistent/tmo/db/schema/claimsSQL'
    stringToBind = 'CLAIMS_AWW.dbo'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'sendgridKey'
    nameInNameSpace = 'tmo/param/sendgridKey'
    stringToBind = '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'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO Shared - httpURLprefixOnlineApps9'
    nameInNameSpace = 'tmo/param/httpURLprefixOnlineApps9'
    stringToBind = 'http://wdeonl9'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO IQ- httpsFQApiUrlPrefix'
    nameInNameSpace = 'tmo/param/httpsFQApiUrlPrefix'
    stringToBind = 'https://quote-api-dev.texasmutual.com'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)

    bindingName = 'TMO IQ- httpsFQWebUrlPrefix'
    nameInNameSpace = 'tmo/param/httpsFQWebUrlPrefix'
    stringToBind = 'https://quote-web-d'
    createStringNameSpaceBinding(scope, bindingName, nameInNameSpace, stringToBind)
    AdminConfig.save()
    sop(m,"Exit success.")


#-----------------------------------------------------------------------
# Setup
#-----------------------------------------------------------------------
def testAndGetNamesBase(cfg):
    """Gets names for the cell, node, server, etc in a single-server environment.
       Stores the values in provided dictionary cfg."""
    m = "testAndGetNamesBase:"
    sop(m,"Entry.")

    # Verify we are running on a single-server.
    env = whatEnv()
    if 'base' != env:
        errbrk(m,"Environment is not 'base'. env=" + env)
    sop(m,"env=" + env)

    # Get cell name.
    cellName = getCellName()
    if 2 > len(cellName):
        errbrk(m,"Cell name is unreasonably small.  cellName=" + cellName)
    sop(m,"cellName=" + cellName)

    # Get node name.
    nodeNameList = getNodeNameList()
    if 1 != len(nodeNameList):
        errbrk(m,"Node name list does not contain exactly one name. nodeNameList=" + nodeNameList)
    nodeName = nodeNameList[0]
    if 2 > len(nodeName):
        errbrk(m,"Node name is unreasonably small.  nodeName=" + nodeName)
    sop(m,"nodeName=" + nodeName)

    # Get server name.
    serverNameList = listAllAppServers()
    if 1 != len(serverNameList):
        errbrk(m,"Server name list does not contain exactly one name. serverNameList=" + serverNameList)
    nodeServerName = serverNameList[0]
    if nodeName != nodeServerName[0]:
        errbrk(m,"Node names to not match. nodeServerName=" + repr(nodeServerName) + " nodeServerName[0]=" + nodeServerName[0])
    serverName = nodeServerName[1]
    if 2 > len(serverName):
        errbrk(m,"Server name is unreasonably small. serverName=" + serverName)
    sop(m,"serverName=" + serverName)

    # Get server ID.
    serverID = getServerByNodeAndName(nodeName,serverName)

    # Verify the server ID string contains recognizable values.
    if not serverID.startswith(serverName):
        errbrk(m,"Server ID does not start with server name. serverID=" + serverID + " serverName=" + serverName)
    if -1 == serverID.find(cellName):
        errbrk(m,"Server ID does not contain the cell name. serverID=" + serverID + " cellName=" + cellName)
    if -1 == serverID.find(nodeName):
        errbrk(m,"Server ID does not contain the node name. serverID=" + serverID + " nodeName=" + nodeName)
    if -1 == serverID.find(serverName):
        errbrk(m,"Server ID does not contain the server name. serverID=" + serverID + " serverName=" + serverName)
    sop(m,"serverID=" + serverID)

    # Save the names for use by other testcases.
    cfg["cellName"] = cellName
    cfg["nodeName"] = nodeName
    cfg["serverName"] = serverName
    cfg["serverID"] = serverID

    sop(m,"Exit success.")

m = "createStringNameSpaceBinding:"
enableDebugMessages()
cfg = {}
sop(m,"Main.")
testAndGetNamesBase(cfg)
dockercreateJAAS(cfg)
dockerCreateStringNameSpaceBinding(cfg)
