# Cybersecurity Hackers do Bem

# Introdução a Cibersegurança

## Áreas de Atuação

- Red Team : Faz testes para descobrir possíveis falhas em sistemas. Utiliza de ferramentas e técnicas para encontrar possíveis falhas. Técnicas como Penetration Testing, Phishing, Engenharia Social.
- Blue Team : Cuida da segurança do sistema
- Forense : Investiga possíveis ataques
- GRC : Responsável por identificar, avaliar, tratar e monitorar os riscos relacionados a cibersegurança
- DevSecOps : Desenvolvimento de softwares de segurança para agilizar o processo entre equipes de trabalho. Responsável por aplicar práticas e principios de segurança como OWASP TOP 10, SANS Top 25

## Vírus

Vírus é um software malicioso que se replica entre sistemas e arquivos.

- Vírus de Arquivo : Anexa-se a arquivos executáveis e se espalha quando esses são executados
- Vírus de Macro : Exploca macros em aplicativos como processadores de texto e planilhas
- Vírus de Boot : Infecta a área de inicialização de um disco rígido tornando-se ativo quando o pc é inicializado
- Worms : diferente de vírus os worms não precisam se anexar a arquivos e podem se espalhar automaticamente pela rede
- Trojans : Disfarçados de softwares legítimos, permitem acesso não autorizado ao sistema

## Medidas preventivas

Antivirus no celular e computador. Evitar abrir arquivos e links suspeitos. Verificar sempre a origem e veracidade de mensagens e remetentes. Escanear dispositivos removíveis. Não fazer download de arquivos suspeitos. Sempre manter todos os softwares atualizados. Fazer backup.

## Ameaças

- SPAM : mensagens eletrônicas não solicitada enviada em massa. É poluição digital e pode ser utilizado para disseminar vírus, spywares.
- Spyware : programa espião que monitora as atividades do usuário na internet. Exemplo é o keyloger. 
- Worms : é semelhante a vírus, pode deletar arquivo, enviar documentos. 
- Phishing : Jogar isca e usuário cai em golpes. 
- Botnets : rede de computadores infectados por malware que permite que um cibercriminoso controle-os remotamente.
- Rootkit : malware furtivo e perigoso que permite que cibercriminosos acessem seu pc sem vc saber
- Ransomware

## Como se proteger

Conceitos essenciais de cibersegurança : privacidade, integridade, disponibilidade e a reputação de dados pessoais.

- Senhas fortes e únicas. 
- Atualizações de sistemas e aplicativos. Atualizações geralmente contém correções de bugs e vulnerabilidades
- Instalar antivírus. 
## Sites de estudo

- Over the Wire
- Try Hack Me

## Ferramenta GoBuster

Com a ferramenta Gobuster conseguimos encontrar endpoints de websites que podem apresentar falhas de segurança importantes

gobuster -u <linkdosite> -w <listaDePalaavrasParaBusca.txt> dir

# Componentes de um Computador

## Grandezas Computacionais

De armezenamento e também de velocidade (por segundo)
- Bit : Menor unidade computacional 0 ou 1
- Byte : Conjunto de 8 bits

## Conversão de Bases

- Base 10 (Decimal)
- Base 16 (Hexadecimal)
- Base 2 (Binária)

Podemos converter com a Notação Posicional. Neste caso pegamos o número e multiplicamos pela base elevada a sua posição. 

Exemplo:

1204 (base 10) para base 10 -->

1x 10^3 + 2x 10^2 + 0x 10^1 + 4x 10^0 = 1000 + 200 + 0 + 4

11110001 (base 2) para base 10 -->
1x 2^7 + 1x 2^6 + 1x2^5 + 1x2^4 + 0 + 0 + 0 + 1 x 2^0 = 128+64+32 + 16 + 1 = 241

3301

Método da divisão - Convertemos de uma base 10 para qualquer uma. 

241/ 4 = 6 sobra 1
60 / 4 = 15 sobra 0
15 / 4 = 3 sobra 3
3 / 4 sobra 3

## Os componentes

CPU : Processador do computador, Unidade Central de Processamento. É o cérebro do computador. Frequência é a velocidade de seu processador. Processadores tem vários núcleos. A memória cache é um tipo de memória auxiliar que faz diminuir tempo de transmissão de infos. Arquiteturas : X86 são 32 bits, X64 de 64 bits ambos CISC e ARM que são RISC.

Placa Mãe : peça fundamental em máquina e é responsável por facilitar a comunicação entre diferentes componentes de computador. 

Memórias : Responsável por armazenar dados de sistema. Papel crucial na velocidade de utilização e troca de dados de computador.
        - Não Voláteis :  ROM, e em massa SSD e HD
        - Voláteis : RAM, Cache, Vídeo
        
BIOS : Basic Input Output System - Nosso SO fica lá.


## Tipos de Conexão

- A sigla DSL significa Digital Subscriber Line e é uma tecnologia utilizada para a transmissão de dados via rede de telefonia. Neste processo, é utilizada uma linha de telefone fixa para fornecer acesso a internet, servindo como uma evolução do serviço dial-up.
- A desvantagem apontada para o PLC é equipamentos chamados HomePlug.
- Internet a cabo: Outra maneira de conexão a internet é através do cabo coaxial, ou cabo trançado.

- Fibra ótica: A conexão de fibra óptica é uma conexão de alta velocidade que se dá através de cabos de vidro ou plástico que realizam a conversão de energia luminosa em elétrica ou sonora. 

## Rede Wan Lan

- Os tipos mais conhecidos de rede de computadores são

        - LAN: Local Area Network, rede local. Compartilhamento de recursos. Controle de acesso. Roteador para rede doméstica e Switch para rede empresarial. 
        - Man : Metropolitan area network. Tipo de malha de comunicação que cobre grande área geográfica. Ligação Fibra óptica. Grande Largura de Banda
        - WAN: Wide Area Network, Rede de longa distancia. Utilizada por empresas com VPN(Virtual private network).
- Para criar rede local precisamos: Determinar quantidade de computadores, quantidade de switch, distancia entre computadores, quantidade de notebooks, definir acesso sem fio, ligar switch em outros

Wireless:

WLAN, WMAN, WPAN, WWAN

-  um switch gerenciável tem a capacidade de ser configurado remotamente e monitorar o tráfego.
- a principal função de um roteador é encaminhar dados entre redes usando endereços IP.
- switches operam na camada dois do modelo OSI e utilizam MAC Address.

## IDS e IPS

O IDS (Sistema de Detecção de Intrusão), sistema responsável por monitorar o tráfego de rede e realizar alertas e notificações em caso de ameaças. Outro exemplo é o IPS (Sistema de Prevenção de Intrusão), responsável por fazer o bloqueio ativo do tráfego malicioso, agindo com uma resposta imediata às ameaças. 