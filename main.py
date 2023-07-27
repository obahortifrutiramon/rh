import pickle
import pandas as pd
import streamlit as st

def previsao(loja,funcao,descricao,sexo,estadoCivil,nacionalidade,grauInstrucao,dependentes,idade):
    with open('RandomForest.pkl', 'rb') as file:
        clf = pickle.load(file)
        
    data = {
        'NOMEFANTASIA': [loja],
        'FUNÇÃO': [funcao],
        'DESCRICAO': [descricao],
        'SEXO': [sexo],
        'DESCRIÇÃO ESTADO CIVIL': [estadoCivil],
        'NACIONALIDADE': [nacionalidade],
        'GRAUINSTRUCAO': [grauInstrucao],
        'N° DEPENDENTES': [dependentes],
        'IDADE': [idade],
    }

    # Formatando os dados para predição
    df_dados = pd.DataFrame(data)
    variaveis_categoricas = ['NOMEFANTASIA','FUNÇÃO','DESCRICAO',
                            'SEXO','DESCRIÇÃO ESTADO CIVIL','NACIONALIDADE','GRAUINSTRUCAO']
    df_dados = pd.get_dummies(df_dados, columns=variaveis_categoricas) # One-hot-encoding
    df_vazio = pd.read_excel('colunas.xlsx')
    df_to_predict = pd.concat([df_vazio, df_dados], ignore_index=True).fillna(0)

    pred = clf.predict(df_to_predict)[0]
    
    if pred == 'Menos de 1 ano':
        return st.error(pred)
    elif pred == 'Acima de 1 ano':
        return st.success(pred)


if __name__ == "__main__":
    # Titulo da pagina
    st.set_page_config(page_title="Avaliação de candidatos")
    
    # Título do aplicativo
    st.title("Avaliação de candidatos\n")
    
    # Texto na página
    st.write("Selecione as opções na menu ao lado e depois clique no botão avaliar para obter a avaliação do candidato para a frente de caixa.")
    
    # Inputs
    loja = st.sidebar.selectbox(label="Loja", 
                                options=['', '01_Oba Carol','02_Oba P.Pta','03_Oba Bonf.','05_Oba Amor.',
                                         '06_Oba Am1','09_Oba Tatu','10_Oba Sor 1','11_Oba But.','12_Oba Ibit.',
                                         '13_Oba Moema','14_Oba Penha','15_Oba Sant.','16_Oba Fruta','17_Oba Mall',
                                         '19_Oba Morum','21_Oba Cent.','23_Oba CB','24_Oba Atal','25_Oba Tolle',
                                         '26_Oba Sor 2','27_Oba Frios','28_Shop Lim','29_Oba Mooca','30_Piracicab',
                                         '31_Oba Sousa','32_Oba VL Ma','33_Oba Galle','34_Oba Anali','35_Oba SJCam',
                                         '36_Oba Angel','37_Oba Teodo','38_Oba Rib','39_Oba Inter','40_Oba Place',
                                         '41_Oba Leopo','42_ST Andre','43_Perdizes','44_306 Nort','45_Colorad',
                                         '46_302 Sud','47_QI09 LA','48_212 Sul','49_Castanh','50_D Bosco','51_Araucar',
                                         '52_209 NOR','53_Flamboy','54_T63','55_CampoBelo','56_VlMascote','57_Jundiai',
                                         '58_VictPires','59_Asa Sul','61_ShpIgutDF','62_Pira Way','63_Shp Jun',
                                         '64_Shpiguaba','65_Ribeirao2','67_SBerCampos','69_Alphavi','70_Oba Frigo',
                                         '71_Whitaker','72_Shop Tatu','73_Cambui2','74_Itaim','75_NovaCps','76_ObaSantos',
                                         '79_Sorocab3','80_Itu','81_Pamplona','84_Oba Tatu3','86_Oba Sao Jose do Rio Preto',
                                         '87_Itatiba','88_Cotia','92_Rest Gr','94_Caixaria','97_Oba CD','99_Oba CD',
                                         '100_CD DF','104_Indaia','107_Oba Am2','108_Oba Lim.','120_Ouro V.',
                                         '121_Oba Arborais','122_BAURU',
                                         ]) #NOMEFANTASIA
    funcao = st.sidebar.selectbox(label="Função", options=['OPERADOR DE CAIXA (LOJA)']) #FUNÇÃO
    descricao = st.sidebar.selectbox(label="Descrição", options=['Frente de Loja']) #DESCRICAO
    sexo = st.sidebar.selectbox(label="Sexo", options=['','Feminino','Masculino']) #SEXO
    estadoCivil = st.sidebar.selectbox(label="Estado civil", options=['','Casado','Desquitado','Divorciado','Separado',
                                                                      'Solteiro','União Estável','Viúvo','Outros']) #ESTADOCIVIL
    nacionalidade = st.sidebar.selectbox(label="Nacionalidade", options=['Brasileiro','Estrangeiro']) #NACIONALIDADE
    #estado = 'GO' #ESTADONATAL
    grauInstrucao = st.sidebar.selectbox(label="Grau de instrução", 
                                         options=['','Analfabeto','Até o 5º ano incompleto do ensino fundamental',
                                                  '5º ano completo do ensino fundamental',
                                                  'Do 6º ao 9º ano do ensino fundamental ',
                                                  'Ensino fundamental completo','Ensino médio incompleto',
                                                  'Ensino médio completo','Educação superior incompleto',
                                                  'Educação superior completo','Pós Grad. incompleto',
                                                  'Pós Grad. completo','Mestrado incompleto','Mestrado completo',
                                                  ]) #GRAUINSTRUCAO
    #cidade = 'Goiânia' #CIDADE
    idade = st.sidebar.number_input('Idade', min_value=0) #N° DEPENDENTES #IDADE
    dependentes = st.sidebar.number_input('Número de dependentes', min_value=0) #N° DEPENDENTES
    
    if st.button('Avaliar'):
        previsao(loja,funcao,descricao,sexo,estadoCivil,nacionalidade,grauInstrucao,dependentes,idade)
    