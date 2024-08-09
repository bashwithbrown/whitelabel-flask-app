import datetime as dt
import os, math, json, uuid, random, string, json


def generate_id(id_type):
    if id_type == 'uuid':
        return str(uuid.uuid4())

    elif id_type == 'string':
        str1 = "".join((random.choice(string.ascii_letters) for _ in range(5)))
        str1 += "".join((random.choice(string.digits) for _ in range(5)))
        sam_list = list(str1)
        random.shuffle(sam_list)
        random_id = "".join(sam_list)
        return random_id

    elif id_type == 'number':
        return random.randint(1, 100000)
    else:
        return None

def allowed_file(filename, allowed_extensions):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions

def log_api_error(logger, exc, request):
    logger.log(
        message=exc, 
        severity='error', 
        meta_data={
        'method': request.method,
        'path': request.path,
        'remote_addr': request.remote_addr,
        'headers': request.headers
    }) 

def get_folder_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size

def convert_file_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])