#!/usr/bin/python -tt
# coding=utf-8

# import all the inbuilt modules
import unittest
import time
import importlib
import sys
import os
import platform

rootDir = os.path.realpath('..')
sys.path.insert(0, rootDir)

# import Device class from uiautomator package
from uiautomator import Device

# Import all the user defined modules
import GlobalConfig
from Framework import Utils

Logger = Utils.loadModule('Framework', 'Logger')
ScreenRecorder = Utils.loadModule('Framework', 'ScreenRecorder')
adb_interface = Utils.loadModule('Framework', 'adb_interface')

# Dynamically import the specified model folder and files
# Serial id of DUT
deviceId = GlobalConfig.MasterDeviceId

UnitPackage = Utils.loadDeviceSpecificModule()
UserConfig = UnitPackage.UserConfig()
Resources = UnitPackage.Resources()

logger = Logger.Logger('Sanity_Wistron_Touch', deviceId, GlobalConfig.LogPath)

Instances = {}
Input = Device(deviceId)
Unit = Utils.initModuleFunction(UnitPackage.Unit, Input, deviceId, UnitPackage, logger, UserConfig, Resources, False, Instances)
UnitUD = Utils.initModuleFunction(UnitPackage.UnitUD, Input, deviceId, UnitPackage, logger, UserConfig, Resources, False, Instances)
Wifi = Utils.initModuleFunction(UnitPackage.Wifi, Input, deviceId, UnitPackage, logger, UserConfig, Resources, False, Instances)
WifiUD = Utils.initModuleFunction(UnitPackage.WifiUD, Input, deviceId, UnitPackage, logger, UserConfig, Resources, False, Instances)
Camera = Utils.initModuleFunction(UnitPackage.Camera, Input, deviceId, UnitPackage, logger, UserConfig, Resources, False, Instances)
CameraUD = Utils.initModuleFunction(UnitPackage.CameraUD, Input, deviceId, UnitPackage, logger, UserConfig, Resources, False, Instances)
Alarm = Utils.initModuleFunction(UnitPackage.Alarm, Input, deviceId, UnitPackage, logger, UserConfig, Resources, False, Instances)
GMS = Utils.initModuleFunction(UnitPackage.GMS, Input, deviceId, UnitPackage, logger, UserConfig, Resources, False, Instances)
GMSUD = Utils.initModuleFunction(UnitPackage.GMSUD, Input, deviceId, UnitPackage, logger, UserConfig, Resources, False, Instances)
Browser = Utils.initModuleFunction(UnitPackage.Browser, Input, deviceId, UnitPackage, logger, UserConfig, Resources, False, Instances)
NFC = Utils.initModuleFunction(UnitPackage.NFC, Input, deviceId, UnitPackage, logger, UserConfig, Resources, False, Instances)
Calendar = Utils.initModuleFunction(UnitPackage.Calendar, Input, deviceId, UnitPackage, logger, UserConfig, Resources, False, Instances)
Settings = Utils.initModuleFunction(UnitPackage.Settings, Input, deviceId, UnitPackage, logger, UserConfig, Resources, False, Instances)
SettingsUD = Utils.initModuleFunction(UnitPackage.SettingsUD, Input, deviceId, UnitPackage, logger, UserConfig, Resources, False, Instances)
Audio = Utils.initModuleFunction(UnitPackage.Audio, Input, deviceId, UnitPackage, logger, UserConfig, Resources, False, Instances)
Email = Utils.initModuleFunction(UnitPackage.Email, Input, deviceId, UnitPackage, logger, UserConfig, Resources, False, Instances)
Messaging = Utils.initModuleFunction(UnitPackage.Messaging, Input, deviceId, UnitPackage, logger, UserConfig, Resources, False, Instances)
Miscellaneous = Utils.initModuleFunction(UnitPackage.Miscellaneous, Input, deviceId, UnitPackage, logger, UserConfig, Resources, False, Instances)
Multimedia = Utils.initModuleFunction(UnitPackage.Multimedia, Input, deviceId, UnitPackage, logger, UserConfig, Resources, False, Instances)
MultimediaUD = Utils.initModuleFunction(UnitPackage.MultimediaUD, Input, deviceId, UnitPackage, logger, UserConfig, Resources, False, Instances)
Ethernet = Utils.initModuleFunction(UnitPackage.Ethernet, Input, deviceId, UnitPackage, logger, UserConfig, Resources, False, Instances)
MTP_PTP = Utils.initModuleFunction(UnitPackage.MTP_PTP, Input, deviceId, UnitPackage, logger, UserConfig, Resources, False, Instances)
Phone = Utils.initModuleFunction(UnitPackage.Phone, Input, deviceId, UnitPackage, logger, UserConfig, Resources, False, Instances)
PhoneUD = Utils.initModuleFunction(UnitPackage.PhoneUD, Input, deviceId, UnitPackage, logger, UserConfig, Resources, False, Instances)
Scanning = Utils.initModuleFunction(UnitPackage.Scanning, Input, deviceId, UnitPackage, logger, UserConfig, Resources, False, Instances)
FileBrowser = Utils.initModuleFunction(UnitPackage.FileBrowser, Input, deviceId, UnitPackage, logger, UserConfig, Resources, False, Instances)
Bluetooth = Utils.initModuleFunction(UnitPackage.Bluetooth, Input, deviceId, UnitPackage, logger, UserConfig, Resources, False, Instances)
NotificationManager = Utils.initModuleFunction(UnitPackage.NotificationManager, Input, deviceId, UnitPackage, logger, UserConfig, Resources, False, Instances)
Adb = adb_interface.AdbInterface(deviceId)

TestRecorder = ScreenRecorder.ScreenRecorder(logger)

class Sanity_Wistron_Touch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        logger.closeLog()

    def setUp(self):
        try:
            logger.log("Set Up")
            self.input = Input
            self.alarm = Alarm
            self.browser = Browser
            self.calendar = Calendar
            self.camera = Camera
            self.cameraUD = CameraUD
            self.email = Email
            self.gms = GMS
            self.gmsUD = GMSUD
            self.messaging = Messaging
            self.multimedia = Multimedia
            self.multimediaUD = MultimediaUD
            self.miscellaneous = Miscellaneous
            self.mtp_PTP = MTP_PTP
            self.phone = Phone
            self.phoneUD = PhoneUD
            self.scanning = Scanning
            self.settings = Settings
            self.settingsUD = SettingsUD
            self.unit = Unit
            self.unitUD = UnitUD
            self.wifi = Wifi
            self.wifiUD = WifiUD
            self.fileBrowser = FileBrowser
            self.Bluetooth = Bluetooth
            self.notificationManager = NotificationManager
            self.nfc = NFC
            self.adb = Adb
            self.audio = Audio
            self.ethernet = Ethernet

            TestRecorder.start(self.id(), self.unit)

            self.unit.unlockScreen()
            self.unit.runAdbCommand("shell settings put global stay_on_while_plugged_in 3")

        except Exception as e:
            print(e)
            logger.setupError(e)
            os._exit(1)

    def tearDown(self):
        logger.log('Tear Down')

        TestRecorder.stop()

        logger.log("Clearing all recent apps")
        self.settings.clearRecentApps()

        self.unit.sendKeyEvent('BACK')
        self.unit.sendKeyEvent('BACK')
        self.unit.sendKeyEvent('HOME')

    def test_001_verify_touch_panel_mode_switch_features_supported(self):
        """
        | **Objective**             : Verify the "Touch panel mode" switch feature supported

        | **Related Bug/Story Id**  : BSPA-54880 / BW-9110 / BW-10611

        | **Test Type**             : Sanity

        | **Test Area(s)**          : None

        | **Required Accessories**  : None

        | **Pre-Setup**             : None

        | **Test Steps**:
        | 1. Go to Settings->Display->Touch panel mode
        | 2. Check below option shows on the screen
        |    Glove and Finger (Screen Protector off)
        |    Stylus and Finger (Screen Protector on)
        |    Glove and Finger (Screen Protector off)
        |    Stylus and Finger (Screen Protector on)
        | 3. Click the options, no reboot found.

        .. Created Date : 05/15/2018
        .. Developer    : GuangweiJiang
        """
        try:
            logger.headerLog(sys._getframe().f_code.co_name, 'BW-9110: Verify the "Touch panel mode" switch feature supported')
            logger.log(sys._getframe().f_code.co_name)

            assert self.unit.openAppAndSettings(UserConfig.SettingApp['text'],[UserConfig.Display['text']]), 'Unable to launch Settings and Display'
            self.input.wait.update()
            time.sleep(1)

            if self.unit.exists(UserConfig.Advanced['text'],scrollable=True):
                assert self.unit.tapOn(UserConfig.Advanced['text'],scrollable=True),'tap on Display Advanced fail'

            assert self.unit.tapOn(uiText=UserConfig.TouchPanelMode['text'],scrollable=True), 'No TouchPanelMode option found'

            self.input.wait.update()
            time.sleep(1)

            assert self.unitUD.VerifyTouchPanelModeList(), 'Verify Touch Panel Mode List failed'

            logger.logPass()

        except Exception as e:
            logger.log(str(e), 'E')
            logger.logFail(collectLogcat=True, collectBugreport=True)

        except KeyboardInterrupt:
            logger.log("Test cancelled by User", 'E')
            logger.logFail(collectLogcat=True, collectBugreport=True)
            logger.closeLog()
            os._exit(1)

    def test_002_Kernel_driver_create_the_same_file_name_on_sysfs(self): #<include USERDEBUGBUILD># #<&&># #<exclude os> OO, PP#
        """
        | **Objective**             : Kernel driver create the same file name on sysfs

        | **Related Bug/Story Id**  : BW-9506

        | **Test Type**             : Sanity

        | **Test Area(s)**          : Sensor

        | **Required Accessories**  : NA

        | **Pre-Setup**             : NA

        | **Test Steps**:
        | 1. Check Touch function work well
        | 2. adb shell
        |    su
        |    For Android O:dmesg > storage/sdcard0/dmesg.txt
        |    For Android Q:dmesg > sdcard0/dmesg.txt
        | 3. shall no error message in dmesg.txt
        |    [    5.458335] {color:red}sysfs: cannot create duplicate filename '//board_properties'{color}

        .. Created Date : 10/06/2020
        .. Developer    : KatieLien
        """
        try:
            print('Sanity_Wistron_Sensor: ' + sys._getframe().f_code.co_name)
            logger.headerLog(sys._getframe().f_code.co_name, 'BW-9506 : Kernel driver create the same file name on sysfs')

            self.unit.runAdbCommand(' shell su root' + "dmesg > sdcard/dmesg.txt", logOutput=False)[1].rstrip()
            self.unitUD.copyFilesToPC(sourceDir=UserConfig.internalSdCard + 'dmesg.txt', targetDir=UserConfig.tempFolderInPC , deviceId=GlobalConfig.MasterDeviceId)

            output = self.unitUD.searchStringInPCFile(filePath=UserConfig.tempFolderInPC + '\\' + 'dmesg.txt', searchString="sysfs: cannot create duplicate filename '//board_properties'")

            if output:
                raise Exception("Kernel should not show error message")

            logger.logPass()

        except Exception as e:
            logger.log(sys._getframe().f_code.co_name + " failed due to " + str(e), 'E')
            logger.logFail(collectLogcat=False, collectBugreport=False, failReason=str(e))
            logger.log('BW-9506' + sys._getframe().f_code.co_name, 'E')

        except KeyboardInterrupt:
            logger.log("Test cancelled by User", 'E')
            logger.logNA("Test cancelled by User")
            logger.closeLog()
            os._exit(1)

    def test_003_Touch_panel_mode_switch_and_Touch_version(self):
        """
        | **Objective**             : Touch panel mode switch and Touch version

        | **Related Bug/Story Id**  : BW-9110

        | **Test Type**             : Sanity

        | **Test Area(s)**          : Sensor

        | **Required Accessories**  : NA

        | **Pre-Setup**             : NA

        | **Test Steps**:
        | 1.Settings->Display->Touch panel mode
        | 2.Switching each touch panel modes.
        | 3.Go to Settings-> System-> About phone-> SW components->Touch, check Touch version and touch mode

        | **Expected Results**:
        | 2.The device should switch each touch panel modes normal.
        | 3a."Mode" show as "Touch panel mode" set in Display.
        | 3b."Version" can not be empty and unkown
        | (eg:Version:1.8.3-Finger-2-0:0x68cffa Mode:Finger Ony)

        .. Created Date : 21/04/2021
        .. Developer    : PellunWu
        """
        try:
            print('Sanity_Wistron_Sensor: ' + sys._getframe().f_code.co_name)
            logger.headerLog(sys._getframe().f_code.co_name, 'BW-9110 : Touch panel mode switch and Touch version')
            checkFlag=False
            for touchPanelMode in UserConfig.TouchPanelModeList:
                #Step:1
                assert self.unit.openAppAndSettings(UserConfig.SettingApp['text'],[UserConfig.Display['text']]), 'Unable to launch Settings and Display'
                if self.unit.exists(UserConfig.Advanced['text'],scrollable=True):
                        assert self.unit.tapOn(UserConfig.Advanced['text'],scrollable=True),'tap on Display Advanced fail'
                assert self.unit.tapOn(UserConfig.TouchPanelMode['text'],scrollable=True), 'No TouchPanelMode option found'
                self.input.wait.update()
                time.sleep(1)
                #Step:2
                if self.unit.exists(touchPanelMode,scrollable=False):
                    assert self.unit.tapOn(touchPanelMode,scrollable=False),'tap on touchPanelMode fail'
                    #Step:3
                    assert self.settingsUD.openAboutPhone(),'Unable open about phone'
                    if self.unit.exists(UserConfig.SWcomponents['text'],scrollable=True):
                        self.unit.tapOn(UserConfig.SWcomponents['text'],scrollable=True)
                    else:
                        raise Exception ("can not find SWComponents")

                    self.unit.scrollScreen(toText=UserConfig.Touch['text'], direction='vertical'),"can not find " + UserConfig.Touch['text']
                    if self.unit.exists(UserConfig.Touch['text'],scrollable=True):
                        value = self.input(text=UserConfig.Touch['text']).sibling(index=1).info[u'text']
                        logger.log ('value = ' + value)

                    if value == '' or value == 'unkown' or value == 'Unkown' or value == 'UNKNOW':
                        raise Exception("Version can not be empty and unkown")
                    else:
                        if touchPanelMode in str(value):
                            checkFlag=True
                            pass
                        else:
                            raise Exception("'Mode' not show as 'Touch panel mode' set in Display")
                else:
                    pass

            if checkFlag is True:
                logger.logPass()
                print("Test Passed")
            else:
                raise Exception("Doesn't find any target in TouchPanelModeList")

        except Exception as e:
            logger.log(sys._getframe().f_code.co_name + " failed due to " + str(e), 'E')
            logger.logFail(collectLogcat=False, collectBugreport=False, failReason=str(e))
            logger.log('BW-9110' + sys._getframe().f_code.co_name, 'E')

        except KeyboardInterrupt:
            logger.log("Test cancelled by User", 'E')
            logger.logNA("Test cancelled by User")
            logger.closeLog()
            os._exit(1)

    def test_004_Compare_Touch_checksum_value(self): #<include USERDEBUGBUILD>#
        """
        | **Objective**             : Compare Touch checksum value

        | **Related Bug/Story Id**  : BW-12422

        | **Test Type**             : Sanity

        | **Test Area(s)**          : Sensor

        | **Required Accessories**  : NA

        | **Pre-Setup**             : NA

        | **Test Steps**:
        | 1. Flash a Eng/Userdebug build image
        | 2.Run command:
        |   adb shell “cat sys/bus/i2c/drivers/atmel_mxt_ts/4-004b/config_csum”,check value
        | 3. Go to Settings-> System-> About phone-> SW components->Touch,check value
        |    The device read checksum value should same as SW components
        |    (eg:Version:1.8.3.0-Finger-2-0:0x68cffa;command read 68cffa)

        .. Created Date : 10/06/2020
        .. Developer    : KatieLien
        """
        try:
            print('Sanity_Wistron_Sensor: ' + sys._getframe().f_code.co_name)
            logger.headerLog(sys._getframe().f_code.co_name, 'BW-12422 : Compare Touch checksum value')

            output = self.unit.runAdbCommand('shell su root "cat sys/bus/i2c/drivers/atmel_mxt_ts/4-004b/config_csum"', logOutput=True)[1].rstrip()
            version = self.settingsUD.getVersionformSWcomponents(UserConfig.Touch['text'])

            logger.log("Adb Command output :" + str(output))
            logger.log("Version form SW components :" + str(version))

            if not str(output) in str(version) :
                raise Exception("The device read checksum value should same as SW components")

            logger.logPass()

        except Exception as e:
            logger.log(sys._getframe().f_code.co_name + " failed due to " + str(e), 'E')
            logger.logFail(collectLogcat=False, collectBugreport=False, failReason=str(e))
            logger.log('BW-12422' + sys._getframe().f_code.co_name, 'E')

        except KeyboardInterrupt:
            logger.log("Test cancelled by User", 'E')
            logger.logNA("Test cancelled by User")
            logger.closeLog()
            os._exit(1)

    def test_005_check_swipe_function_top_bottom(self):
        """
        | **Objective**             : Check swipe function to top and bottom

        | **Related Bug/Story Id**  : Build Daily Sanily - TouchPanelTest

        | **Test Type**             : Sanity

        | **Test Area(s)**          : None

        | **Required Accessories**  : None

        | **Pre-Setup**             : None

        | **Test Steps**:
        | 1. Open the setting
        | 2. Scroll to the bottom
        | 3. Check the text of SettingsSystem which is existing
        | 4. Scroll to the top
        | 5. Check the text of NetworkNInternetText which is existing

        .. Created Date : 04/13/2018
        .. Developer    : ChaojunLu
        """
        try:
            logger.headerLog(sys._getframe().f_code.co_name, "check swipe function top and bottom")
            logger.log(sys._getframe().f_code.co_name)

            assert self.unit.launchApp(UserConfig.SettingApp['text']),"unable open Setting"

            assert self.unit.scrollScreen(toStartOrEnd='End'),"unable scroll to bottom"
            time.sleep(2)

            assert self.unit.exists(UserConfig.SettingsSystem['text'],scrollable=False),'SettingsSystem is not existing'
            time.sleep(2)

            for i in range(3):
                assert self.unitUD.swipeFromCenterToOutside('down'), "swipeFromCenterToOutside failed"
                time.sleep(2)

            assert self.unit.exists(UserConfig.NetworkAndInternet['text'],scrollable=False),'NetworkAndInternet is not existing'
            time.sleep(2)

            logger.logPass()

        except Exception as e:
            logger.log(sys._getframe().f_code.co_name + " failed due to " + str(e), 'E')
            logger.logFail(collectLogcat=False, collectBugreport=False, failReason=str(e))
            logger.log('test_003_check_baseband_version_is_not_none' + sys._getframe().f_code.co_name, 'E')

        except KeyboardInterrupt:
            logger.log("Test cancelled by User", 'E')
            logger.logNA("Test cancelled by User")
            logger.closeLog()
            os._exit(1)

    def test_006_check_swipe_function_left_right(self): #<exclude model> TC72, TC52#
        """
        | **Objective**             : Check swipe function to right and left

        | **Related Bug/Story Id**  : Build Daily Sanily - TouchPanelTest

        | **Test Type**             : Sanity

        | **Test Area(s)**          : None

        | **Required Accessories**  : None

        | **Pre-Setup**             : None

        | **Test Steps**:
        | 1. Open the setting
        | 2. Scroll to the right
        | 3. Check the text of Contact which is existing
        | 4. Scroll to the left
        | 5. Check the text of SpeedDial which is existing

        .. Created Date : 04/23/2018
        .. Developer    : BonnieChen
        """
        try:
            logger.headerLog(sys._getframe().f_code.co_name, "check swipe function left and right")
            logger.log(sys._getframe().f_code.co_name)
            #RebootDevice make sure clock app status original
            t0 = time.perf_counter()
            self.unit.rebootDevice()
            self.adb.WaitForBootComplete()
            rebootDuration = time.perf_counter()-t0
            if rebootDuration>180:
                raise Exception("boot up time too long")
            self.unit.unlockScreen()
            assert self.unit.launchApp(UserConfig.ClockApp['text']), "unable launch phone app"
            if self.unit.exists(UserConfig.Allow['text']):
                self.unit.tapOn(UserConfig.Allow['text'],scrollable=False)
            assert self.unitUD.checkSwipeRight(),"unable swipe right"
            assert self.unitUD.checkSwipeLeft(),"unable swipe left"

            logger.logPass()

        except Exception as e:
            logger.log(sys._getframe().f_code.co_name + " failed due to " + str(e), 'E')
            logger.logFail(collectLogcat=False, collectBugreport=False, failReason=str(e))
            logger.log('test_003_check_baseband_version_is_not_none' + sys._getframe().f_code.co_name, 'E')

        except KeyboardInterrupt:
            logger.log("Test cancelled by User", 'E')
            logger.logNA("Test cancelled by User")
            logger.closeLog()
            os._exit(1)

    def test_007_check_drag_drop_Icon(self): #<exclude ngms>#
        """
        | **Objective**             : Drag and drop the icon

        | **Related Bug/Story Id**  : Build Daily Sanily - TouchPanelTest

        | **Test Type**             : Sanity

        | **Test Area(s)**          : None

        | **Required Accessories**  : None

        | **Pre-Setup**             : None

        | **Test Steps**:
        | 1. Drag the Calculator App
        | 2. Check the text of Calculator which is existing
        | 3. Remove the Calculator APP icon

        .. Created Date : 04/13/2018
        .. Developer    : ChaojunLu
        """
        try:
            logger.headerLog(sys._getframe().f_code.co_name, "Check draging and dropping the icon")
            logger.log(sys._getframe().f_code.co_name)

            self.unitUD.unlockScreen()
            self.unit.sendKeyEvent('HOME')

            self.devHeight=self.input.info['displayHeight']
            self.devWidth=self.input.info['displayWidth']

            assert self.unitUD.swipeFromOutsideToCenter('up'),"unable open the app list"
            time.sleep(2)

            assert self.unit.dragTo(src="Calculator",dest=(self.devWidth/2, self.devHeight/2)),"unable drag the Calculator"
            time.sleep(2)

            assert self.unit.exists(UserConfig.CalculatorText['text'],scrollable=False),'Calculator APP is not existing'
            time.sleep(2)

            if GlobalConfig.MasterAndroidVersion=='OO':
                self.unit.dragTo(src=UserConfig.CalculatorText['text'],dest=(200,120))
            else:
                self.unit.dragTo(src=UserConfig.CalculatorText['text'],dest=(self.devWidth/2, 120))

            assert not self.unit.exists(UserConfig.CalculatorText['text'],scrollable=False),'Calculator APP is existing'
            logger.logPass()

        except Exception as e:
            logger.log(sys._getframe().f_code.co_name + " failed due to " + str(e), 'E')
            logger.logFail(collectLogcat=False, collectBugreport=False, failReason=str(e))
            logger.log('test_003_check_baseband_version_is_not_none' + sys._getframe().f_code.co_name, 'E')

        except KeyboardInterrupt:
            logger.log("Test cancelled by User", 'E')
            logger.logNA("Test cancelled by User")
            logger.closeLog()
            os._exit(1)

        finally:
            self.unitUD.removeEmailApp()

    def test_008_zoom_in_out_photo_by_finger(self):
        """
        | **Objective**             : Zoom in/out photo by finger

        | **Related Bug/Story Id**  : Build Daily Sanily - TouchPanelTest

        | **Test Type**             : Sanity

        | **Test Area(s)**          : None

        | **Required Accessories**  : None

        | **Pre-Setup**             : None

        | **Test Steps**:
        | 1. Push the photo to android device
        | 2. Launch the Photos app
        | 3. Tap on the test.jpg
        | 4. Zoom out/in the photo
        | 5. check the photo after zooming in/out
        | 6. Delete the photo

        .. Created Date : 04/19/2018
        .. Developer    : ChaojunLu
        """
        try:
            logger.headerLog(sys._getframe().f_code.co_name, "Check zooming in/out the photo")
            logger.log(sys._getframe().f_code.co_name)

            assert self.cameraUD.deleteCameraAllImageVideos(), 'unable delete camera image and videos'

            time.sleep(5)
            assert self.unitUD.copyFilesToAndroidDevice(Resources.test_jpg,UserConfig.cameraFolderAndroidInternalSD),"unable copy the Image files to android device"
            time.sleep(2)
            self.unit.runAdbCommand(' shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/DCIM/Camera/test.jpg')
            time.sleep(2)

            self.unitUD.checkZoomInOutPhoto()

            logger.logPass()

        except Exception as e:
            logger.log(sys._getframe().f_code.co_name + " failed due to " + str(e), 'E')
            logger.logFail(collectLogcat=False, collectBugreport=False, failReason=str(e))
            logger.log('test_003_check_baseband_version_is_not_none' + sys._getframe().f_code.co_name, 'E')

        except KeyboardInterrupt:
            logger.log("Test cancelled by User", 'E')
            logger.logNA("Test cancelled by User")
            logger.closeLog()
            os._exit(1)

        finally:
            self.unitUD.removeTestPhoto()


    def test_009_Clicking_a_folder_in_the_Files_app_with_the_stylus(self):
        """
        | **Objective**             : Clicking a folder in the Files app with the stylus

        | **Related Bug/Story Id**  : BW-4409

        | **Test Type**             : Sanity

        | **Test Area(s)**          : touch

        | **Required Accessories**  : NA

        | **Pre-Setup**             : NA

        | **Test Steps**:
        |1.Take the device with latest build.
        |2.Settings -> Display >TouchPanelUI > Select touch mode as "Stylus & Finger"
        |3. Navigate to home using Stylus 
        |4.Launch Files application using Stylus.
        |5. Navigate to folders page click on the any folder using stylus.

        | **Expected Results**:
        |3&4&5.stylus functionality should work fine

        .. Created Date : 011/05/2021
        .. Developer    : Bill Dong
        """
        try:
            logger.headerLog(sys._getframe().f_code.co_name, 'BW-4409:  Clicking a folder in the Files app with the stylus')
            logger.log(sys._getframe().f_code.co_name)

            logger.log('Opening System in SettingsAPP')
            self.input.wait.update()
            hardwareVerAdb = self.unit.runAdbCommand('shell getprop |grep ro.config.device.hwrev')[1].rstrip()

            assert self.unit.openAppAndSettings(UserConfig.SettingApp['text'],UserConfig.Display['text']), "Unable to launch Settings App"

            if self.unit.exists(uiText=UserConfig.Advanced['text'], scrollable=True):
               self.unit.tapOn(UserConfig.Advanced['text'],scrollable=True)

            if self.unit.exists(UserConfig.TouchPanelMode['text'],scrollable=True):
                self.unit.tapOn(UserConfig.TouchPanelMode['text'],scrollable=True)
                print("Find TouchPanelUI")

            if self.unit.existsSubImage("../Resources/touchpanel/SAF_SPOFF_1080.png"):
                assert self.unit.tapOnImage("../Resources/touchpanel/SAF_SPOFF_1080.png", threshold=0.2), 'No Stylus and Finger (Screen Protector on) to tap'
                self.input.wait.update()
                time.sleep(2)
            else:
                raise Exception("No Stylus and Finger (Screen Protector on) not exist")

            assert self.unit.launchApp(UserConfig.Files['text']),"Unable to launch Files App"
            assert self.unit.tapOn(uiDescription=UserConfig.ShowRoots['description'], ClassName=UserConfig.ShowRoots['className']), "Unable to click Show roots"
            self.input.wait.update()
            time.sleep(1)


            if self.unit.exists(GlobalConfig.MasterModel != 'MC93' or GlobalConfig.MasterModel !='MC93C'):
                assert self.unit.tapOn(GlobalConfig.MasterModel,scrollable=True), "not find Master device folder"
                assert self.unit.tapOn(UserConfig.ZebraVolumeAlarm['description'],scrollable=True), "not find Alarm folder"
            elif GlobalConfig.MasterModel == 'MC93' or GlobalConfig.MasterModel == 'MC93C':
                assert self.unit.tapOnPartial(uiText='MC93',scrollable=True), "not find Master device folder"
                assert self.unit.tapOn(UserConfig.ZebraVolumeAlarm['description'],scrollable=True), "not find Alarm folder"

            logger.logPass()
            print("Test Passed")

        except Exception as e:
            logger.log(sys._getframe().f_code.co_name + " failed due to " + str(e), 'E')
            logger.logFail(collectLogcat=False, collectBugreport=False, failReason=str(e))
            logger.log('test_003_check_baseband_version_is_not_none' + sys._getframe().f_code.co_name, 'E')

        except KeyboardInterrupt:
            logger.log("Test cancelled by User", 'E')
            logger.logNA("Test cancelled by User")
            logger.closeLog()
            os._exit(1)

if __name__ == '__main__':
    unittest.main()

    # To simulate Force close activity-> adb shell am start -n com.android.contacts/com.android.contacts.activities.ContactEditorActivity
