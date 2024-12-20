#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2005-2009, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

import os
import sys
import datetime

def I18N_NOOP(x):
    return x

def size_fmt(size):
    parts = []
    if size == 0:
        return "0"
    while size > 0:
        parts.append("%03d" % (size % 1000))
        size /= 1000
    parts.reverse()
    tmp = ".".join(parts)
    return tmp.lstrip("0")

def xterm_title(message, log_dir="logs"):
    """Set message as console window title."""
    if os.environ.has_key("TERM") and sys.stderr.isatty():
        terminalType = os.environ["TERM"]
        for term in ["xterm", "Eterm", "aterm", "rxvt", "screen", "kterm", "rxvt-unicode"]:
            if terminalType.startswith(term):

                sys.stderr.write("\x1b]2;"+str(message)+"\x07")
                sys.stderr.flush()
                break
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Log the message to a file with timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    log_file = os.path.join(log_dir, "{0}_log.txt".format(timestamp))
    with open(log_file, "a") as f:
        log_entry = "%s %s\n" % (timestamp, message)
        f.write(log_entry)
        f.flush()
    

def wait_bus(unix_name, timeout=5, wait=0.1, stream=True):
    import socket
    import time
    if stream:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    else:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    while timeout > 0:
        try:
            sock.connect(unix_name)
            return True
        except:
            timeout -= wait
        time.sleep(wait)
    return False
