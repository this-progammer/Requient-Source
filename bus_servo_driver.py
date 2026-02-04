####################################################################
#
#   Application : MaxArm ESP32 Tools
#   
#   Add : Praise the Lord, not me
#
#   Programmer : Hunter M.
#
#   Use Of Code : This code is to write Software to control ESP32 MaxArm Robot, intended for, New Prairie High School
#
####################################################################

class Bus_Servo_Driver:
    
    _typecmpname = 'Hiwonder'
    busServo = 'BUS SERVO'
    espDriverType = 'ESP32-S'
    esp_FCC_ID = '2AHMR-ESP32-S'
    esp_CMIIT_ID = '2019DP8469'
    esp_WIFI_BT = 'SoC Inside'
    
    espServoON = bool
    espServoOFF = bool
    espBLUETOOTHMode = bool
    espPOWERAble = bool
    
    def proc_get_cmpname( servo )->str:
        return servo._typecmpname
    
    def proc_get_bus_servo( servo )->str:
        return servo.busServo
    
    def proc_get_esp_driver_type( servo )->str:
        return servo.espDriverType
    
    def proc_get_fcc_id( servo )->str:
        return servo.esp_FCC_ID
    
    def proc_get_cmiit_id( servo )->str:
        return servo.esp_CMIIT_ID
    
    def proc_get_wifi_bt( servo )->str:
        return servo.esp_WIFI_BT
    
    def proc_get_bluetooth_driver( servo )->str:
        return servo.espBLUETOOTHMode
    
    def __busProc_decl_power( servo )->bool:
        if( servo.espPOWERAble == True and not False ):
            return servo.espServoON == True
        else:
            return servo.espServoOFF == True
        
        return servo.espPOWERAble
    
    def __bus_driver_stream_message_s( s ):
        return print( s )
    
    
class BusMemory:
    
    def bmemoryset( servo ):
        memorymanager = set()
        for memvariable in range( 0 ):
            memorymanager.add( servo )
            if servo == 0:
                memorymanager.update()
                memorymanager.discard( servo )
                
def callBusMemory( bus : BusMemory ):
    return bus