# src/source_sftp.py
import paramiko
from pathlib import Path

def fetch_sftp_files(
    host,
    port,
    username,
    password,
    remote_path,
    local_path="data/raw_input"
):
    local_dir = Path(local_path)
    local_dir.mkdir(parents=True, exist_ok=True)

    transport = None
    sftp = None
    downloaded_files = []
    failed_files = []

    try:
        transport = paramiko.Transport((host, port))
        transport.connect(username=username, password=password)

        sftp = paramiko.SFTPClient.from_transport(transport)

        for file_attr in sftp.listdir_attr(remote_path):
            if not file_attr.filename.startswith("."):
                remote_file = f"{remote_path}/{file_attr.filename}"
                local_file = local_dir / file_attr.filename

                try:
                    sftp.get(remote_file, str(local_file))
                    downloaded_files.append(local_file)
                except Exception as e:
                    failed_files.append((file_attr.filename, str(e)))

    except Exception as e:
        failed_files.append(("connection_error", str(e)))

    finally:
        if sftp:
            sftp.close()
        if transport:
            transport.close()

    return downloaded_files, failed_files
