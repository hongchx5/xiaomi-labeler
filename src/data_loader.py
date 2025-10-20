# ...existing code...
import pandas as pd
import io

def _try_read(path, encoding):
    return pd.read_csv(path, encoding=encoding)

def load_data(file_path):
    """
    读取 CSV，尝试多种编码以避免 UnicodeDecodeError。
    返回 pandas.DataFrame。
    """
    encodings_to_try = ["utf-8", "gbk", "cp1252", "latin1"]
    # 如果 chardet 可用，可以先尝试检测（可选）
    try:
        import chardet
        with open(file_path, "rb") as f:
            raw = f.read(40960)
            guess = chardet.detect(raw)
            if guess and guess.get("encoding"):
                encodings_to_try.insert(0, guess["encoding"])
    except Exception:
        pass

    last_exc = None
    for enc in encodings_to_try:
        try:
            df = _try_read(file_path, encoding=enc)
            # 成功读取后返回
            return df
        except UnicodeDecodeError as e:
            last_exc = e
            continue
        except Exception as e:
            # 其它错误也记录但继续尝试下一个编码
            last_exc = e
            continue

    # 如果都失败，抛出最后一个异常（便于上层看到具体信息）
    raise last_exc or UnicodeDecodeError("unknown", b"", 0, 1, "failed to detect encoding")


def save_data(df, file_path):
    """
    保存 DataFrame 到 CSV，使用 UTF-8 编码（不保存索引）。
    """
    df.to_csv(file_path, index=False, encoding="utf-8")
# ...existing code...