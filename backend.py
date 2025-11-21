import numpy as np
from scipy.signal import spectrogram, windows

# 1. Fungsi Menghitung FFT Global
def compute_global_fft(signal, fs):
    n = len(signal)
    if n == 0:
        return np.array([]), np.array([])
    
    nfft = int(2 ** np.ceil(np.log2(n)))
    S = np.fft.rfft(signal, n=nfft)
    freqs = np.fft.rfftfreq(nfft, d=1.0/fs)
    amps = np.abs(S) / n
    
    return freqs, amps

# 2. Fungsi Spektrogram + JEJAK DOMINAN
def compute_spectrogram_with_trace(signal, fs, nperseg=512, noverlap=None):
    if signal is None:
        return None, None, None, None
        
    if noverlap is None:
        noverlap = nperseg // 2
    
    # Hitung Spektrogram
    f, t, Sxx = spectrogram(signal, fs=fs, window='hann',
                            nperseg=nperseg, noverlap=noverlap,
                            scaling='spectrum', mode='magnitude')
    
    # Cari frekuensi dominan di setiap waktu
    max_indices = np.argmax(Sxx, axis=0) 
    dom_freqs = f[max_indices]
    
    return f, t, Sxx, dom_freqs

# 3. Fungsi FFT Lokal (Untuk Panel ke-3)
def local_fft(signal, fs, center_idx, window_size):
    n = len(signal)
    half = window_size // 2
    start = max(0, center_idx - half)
    end = min(n, center_idx + half)
    
    seg = signal[start:end]
    if len(seg) < 8:
        return None
    
    w = windows.hann(len(seg))
    segw = seg * w
    
    nfft = int(2 ** np.ceil(np.log2(len(segw))))
    S = np.fft.rfft(segw, n=nfft)
    freqs = np.fft.rfftfreq(nfft, d=1.0/fs)
    amps = np.abs(S) / len(segw)
    
    idx_max = np.argmax(amps)
    
    return {
        "start": start, 
        "end": end,
        "freqs": freqs, 
        "amps": amps,
        "dominant_frequency": float(freqs[idx_max])
    }
