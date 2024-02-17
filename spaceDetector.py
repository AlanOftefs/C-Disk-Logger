import psutil
def GetDiskInfo():
    disk_used = {}
    for id in psutil.disk_partitions():
        if 'cdrom' in id.opts or id.fstype == '':
            continue
        disk_name = id.device.split(':')
        s = disk_name[0]
        if s == 'C':
            disk_info = psutil.disk_usage(id.device)
            return disk_info.free    
