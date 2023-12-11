from Foundation import NSObject, NSApplicationDelegate


def NSApplicationDelegate():
    class YourAppDelegate(NSObject, NSApplicationDelegate):
        def applicationSupportsSecureRestorableState_(self, app):
            return True

    # Создайте экземпляр вашего делегата
    delegate = YourAppDelegate.alloc().init()

    # Задайте его в качестве делегата вашему NSApplication
    NSApp().setDelegate_(delegate)