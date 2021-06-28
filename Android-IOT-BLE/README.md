# BLE(Bluetooth Low Energy)(bluetooth smart)
* BLE 지원하는 디바이스들은 기본적으로 Advertise(Brroacast) 과 Connection이라는 방법으로 외부와 통신한다   
    * Advertis Mode(=Broadcast Mode)    
        특정 드바이스를 지정하지 않고 주변의 모든 디바이스에게 signal을 보낸다 다시 말해 주변에 디바이스가 있건 없건 다른 디바이스가 signal을 듣는 상태이건 아니건 자신의 signal을 일방적으로 보내는 것이라고 하며 일정주기로 보낸다
        * Advertiser : Non - Connectable Advertising Packet을 주기적으로 보내는 다비이스
        * Observer : Advertiser가 Adevertis르 Non _connectable Advertising Packet을 듣기 위해 주기적으로 Scanning하는 디바이스
    * Connection Mode : Advertise처럼 일대 다의 관계를 이루지 않고 일 대 일 관계를 이루고 있다!!
* BLE용어 정리!!
    * GATT(Generic  Attribute Profile) : GATT는 두 BLE 자치간에 Service , Characteristic을 이용하여 데이터를 주고 받는 방법을 정의 하는것
        * GATT기반 동작 구조는 Profile > Service > Characteristic에 기초 합니다!! 
            * Profile : 정의된 서비스의 묶음으로 그저 이름이라고 생각!!
            * Service : 데이터를 논리적인 단위를 나누는 역할을 하며 특성(charactericstic) 이라 불리는 데이터 단위를 하나이상 포함하고 있습니다!!<strong>각 서비스는 UUID라 불리는 16bit은 128bit 구분자를 가진다</strong>
            * characteristic : 특성은 단하나의 데이터를 포함합니다
    * Attribute Protocol(ATT) : GATT는 ATT의 최상위 구현체이며 GATT/ATT로 참조된다 . 각각의 속성(Attribute)은 UUID가지며 128비트로 구성됩나다. ATT에 의해 부여된 속성은 특성(Characteristic)과 서비스를 결정합니다!
    * Service : 하나의 서비스는 특성들의 집합입니다.
    * Characteristic : 하나의 특성(Characterstic)은 하나의 값과 n개의 디스크립터를 포함합니다!
    * Descripter : 디스크립터는 특성의 값을 기술한다!
* 전체적인 흐름에서의 용어 정리!!
    * central : Scanning, 게시검색을 담담함
    * Peripheral : 게시(advertisement)를 만든다!!    
* 휴대폰과 센서 장치를 BLE 로 연결할때 휴대폰은 센서 장치를 scan하므로 central이 되고 센서장치는 게시하기 때문에 peripheral이 됩니다!  
