# cuts
#cuts = {}
#supercut='1'
supercut='\
abs(std_vector_jet_eta[1])<5 && abs(std_vector_jet_eta[0])<5 \
&& metPfType1 > 30 \
&& std_vector_jet_pt[0]>30 && std_vector_jet_pt[1]>30 \
&& (abs((std_vector_lepton_eta[0] - (std_vector_jet_eta[0]+std_vector_jet_eta[1])/2)/detajj) < 0.5) \
&& (abs((std_vector_lepton_eta[1] - (std_vector_jet_eta[0]+std_vector_jet_eta[1])/2)/detajj) < 0.5) \
&& veto_EMTFBug'
#&& (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1]) > 0 '

           

#cuts['VBS_13TeV_SS']='(std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1]) > 0'
#cuts['VBS_13TeV_BaseCut']='1'

 
# cuts['VBS_13TeV_BaseCut_eMu']='std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == 11*13' 
#cuts['VBS_13TeV_BaseCut_ee']='std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == 11*11' 
#cuts['VBS_13TeV_BaseCut_MuMu']='std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == 13*13' 

tauVeto = '\
( std_vector_tau_pt[0] < 18 || std_vector_tau_looseIso_dbeta[0] < 1. || (sqrt( pow(std_vector_tau_eta[0] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[0] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[0] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[0] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) \
&& ( std_vector_tau_pt[1] < 18 || std_vector_tau_looseIso_dbeta[1] < 1. || (sqrt( pow(std_vector_tau_eta[1] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[1] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[1] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[1] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) \
&& ( std_vector_tau_pt[2] < 18 || std_vector_tau_looseIso_dbeta[2] < 1. || (sqrt( pow(std_vector_tau_eta[2] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[2] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[2] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[2] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) \
&& ( std_vector_tau_pt[3] < 18 || std_vector_tau_looseIso_dbeta[3] < 1. || (sqrt( pow(std_vector_tau_eta[3] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[3] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[3] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[3] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) \
&& ( std_vector_tau_pt[4] < 18 || std_vector_tau_looseIso_dbeta[4] < 1. || (sqrt( pow(std_vector_tau_eta[4] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[4] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[4] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[4] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) \
&& ( std_vector_tau_pt[5] < 18 || std_vector_tau_looseIso_dbeta[5] < 1. || (sqrt( pow(std_vector_tau_eta[5] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[5] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[5] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[5] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) \
&& ( std_vector_tau_pt[6] < 18 || std_vector_tau_looseIso_dbeta[6] < 1. || (sqrt( pow(std_vector_tau_eta[6] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[6] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[6] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[6] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) \
&& ( std_vector_tau_pt[7] < 18 || std_vector_tau_looseIso_dbeta[7] < 1. || (sqrt( pow(std_vector_tau_eta[7] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[7] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[7] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[7] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) \
&& ( std_vector_tau_pt[8] < 18 || std_vector_tau_looseIso_dbeta[8] < 1. || (sqrt( pow(std_vector_tau_eta[8] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[8] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[8] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[8] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) \
&& ( std_vector_tau_pt[9] < 18 || std_vector_tau_looseIso_dbeta[9] < 1. || (sqrt( pow(std_vector_tau_eta[9] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_tau_phi[9] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3 || sqrt( pow(std_vector_tau_eta[9] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_tau_phi[9] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) )\
'
            

BVeto = '\
( std_vector_jet_pt[0] < 20 || (std_vector_jet_csvv2ivf[0] < 0.8484 )  ) \
&& ( std_vector_jet_pt[1] < 20 || (std_vector_jet_csvv2ivf[1] < 0.8484 )  ) \
&& ( std_vector_jet_pt[2] < 20 || (std_vector_jet_csvv2ivf[2] < 0.8484 )  ) \
&& ( std_vector_jet_pt[3] < 20 || (std_vector_jet_csvv2ivf[3] < 0.8484 )  ) \
&& ( std_vector_jet_pt[4] < 20 || (std_vector_jet_csvv2ivf[4] < 0.8484 )  ) \
&& ( std_vector_jet_pt[5] < 20 || (std_vector_jet_csvv2ivf[5] < 0.8484 )  ) \
&& ( std_vector_jet_pt[6] < 20 || (std_vector_jet_csvv2ivf[6] < 0.8484 )  ) \
&& ( std_vector_jet_pt[7] < 20 || (std_vector_jet_csvv2ivf[7] < 0.8484 )  ) \
&& ( std_vector_jet_pt[8] < 20 || (std_vector_jet_csvv2ivf[8] < 0.8484 )  ) \
&& ( std_vector_jet_pt[9] < 20 || (std_vector_jet_csvv2ivf[9] < 0.8484 )  ) \
'
#csvv2ivf combined secondary vertex alghortim. Higher values means a better probability of tagging a b-jet
softMuVeto='\
&& ( std_vector_softMuPt[0] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[0] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[0] - std_vector_lepton_phi[0])-pi)-pi, 2) )< 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[0] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[0] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) \
&& ( std_vector_softMuPt[1] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[1] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[1] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[1] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[1] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) \
&& ( std_vector_softMuPt[2] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[2] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[2] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[2] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[2] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) \
&& ( std_vector_softMuPt[3] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[3] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[3] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[3] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[3] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) \
&& ( std_vector_softMuPt[4] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[4] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[4] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[4] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[4] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) \
&& ( std_vector_softMuPt[5] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[5] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[5] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[5] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[5] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) \
&& ( std_vector_softMuPt[6] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[6] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[6] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[6] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[6] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) \
&& ( std_vector_softMuPt[7] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[7] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[7] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[7] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[7] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) \
&& ( std_vector_softMuPt[8] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[8] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[8] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[8] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[8] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) \
&& ( std_vector_softMuPt[9] < 3 || ((abs(std_vector_lepton_flavour[0]) == 13. && sqrt( pow(std_vector_softMuEta[9] - std_vector_lepton_eta[0], 2) + pow(abs(abs(std_vector_softMuPhi[9] - std_vector_lepton_phi[0])-pi)-pi, 2) ) < 0.3) || (abs(std_vector_lepton_flavour[1]) == 13. && sqrt( pow(std_vector_softMuEta[9] - std_vector_lepton_eta[1], 2) + pow(abs(abs(std_vector_softMuPhi[9] - std_vector_lepton_phi[1])-pi)-pi, 2) ) < 0.3 ) ) ) \
'
bJetVeto = BVeto # + softMuVeto
bJetTag  = '!(' + bJetVeto + ')'  

#cuts['VBS_13TeV_TauVeto']=tauVeto

#cuts['VBS_13TeV_bJetVeto']=bJetVeto

#cuts['VBS_13TeV_bJetTag']=bJetTag

zveto ='mll>20 && (abs(std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1]) != 11*11 || abs(mll - 91) > 15)'
#cuts['VBS_13TeV_Zveto_ee']=zveto + '&& std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == 11*11'
#cuts['VBS_13TeV_Zveto']=zveto 
#cuts['VBS_13TeV_Zveto_LL']=zveto + '&& (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == 11*11 || std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == 13*13)' 
#cuts['VBS_13TeV_Zveto_eMu']=zveto + '&& std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == 11*13' 


cuts['VBS_13TeV_AllVetoes']  =zveto + '&&' + tauVeto +'&&'+ bJetVeto  
cuts['VBS_13TeV_AllVetoes_Positive']  =zveto + '&&' + tauVeto +'&&'+ bJetVeto + '&& std_vector_lepton_flavour[0]>0'
cuts['VBS_13TeV_AllVetoes_Negative']  =zveto + '&&' + tauVeto +'&&'+ bJetVeto + '&& std_vector_lepton_flavour[0]<0'
# 11 = e
# 13 = mu
# 15 = tau


