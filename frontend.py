import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from tkinter import filedialog, Tk
import backend 
import importlib
importlib.reload(backend)

# --- FUNGSI KLIK ---
def on_click(event):
    # Hanya respon kalau klik di panel paling bawah (Spectrogram)
    if event.inaxes != ax_spec: return

    click_time = event.xdata
    idx = int(click_time * fs)
    
    # Panggil backend
    res = backend.local_fft(data, fs, idx, window_size=1024)
    
    if res is not None:
        loc_freqs = res['freqs']
        loc_amps = res['amps']
        start = res['start']
        end = res['end']
        dom_freq = res['dominant_frequency']
        
        # --- UPDATE PANEL 3 (Analisis FFT Lokal) ---
        ax_local.clear()
        # Plot FFT Lokal (Merah)
        ax_local.plot(loc_freqs, loc_amps, color='red', linewidth=1.5, label='Lokal Spectrum')
        
        # Tambahkan bayangan FFT Global (Biru tipis) buat perbandingan
        ax_local.plot(freqs, amps, color='blue', alpha=0.1, linewidth=0.5, label='Global (Ref)')
        
        ax_local.legend(loc='upper right')
        ax_local.set_title(f"3. Analisis FFT Detik ke-{click_time:.2f} (Dominan: {dom_freq:.1f} Hz)")
        ax_local.set_ylabel("Magnitude")
        ax_local.grid(True, alpha=0.3)
        
        # --- UPDATE PENANDA VISUAL ---
        # Hapus garis putih lama
        lines = [line for line in ax_spec.get_lines() if line.get_color() == 'white']
        for line in lines: line.remove()
            
        for patch in ax_time.patches: patch.remove()
        
        # Gambar garis baru
        ax_spec.axvline(x=click_time, color='white', linestyle='--', alpha=0.8)
        ax_time.axvspan(start/fs, end/fs, color='red', alpha=0.3)
        
        plt.draw()

# --- MAIN PROGRAM ---

root = Tk()
root.withdraw()
print("Pilih file audio (.wav)...")
file_path = filedialog.askopenfilename(title="Pilih Audio File", filetypes=[("Audio", "*.wav *.flac")])

if not file_path:
    exit()

# Load Data
data, fs = sf.read(file_path)
if data.ndim > 1: data = data[:, 0]

# Hitung Backend
freqs, amps = backend.compute_global_fft(data, fs)
f_spec, t_spec, Sxx, dom_freqs = backend.compute_spectrogram_with_trace(data, fs)

# --- SETUP 4 PANEL ---
# figsize diperbesar (tinggi 12) biar muat 4 grafik
fig, (ax_time, ax_global, ax_local, ax_spec) = plt.subplots(4, 1, figsize=(10, 12), 
                                                constrained_layout=True, 
                                                height_ratios=[0.8, 1, 1, 1.5])
fig.canvas.manager.set_window_title('Analisis Sinyal Audio (4 Output)')

# 1. OUTPUT PERTAMA: Sound Raw (Time Domain)
ax_time.plot(np.arange(len(data))/fs, data, linewidth=0.5, color='black')
ax_time.set_title("1. Sinyal Asli (Time Domain)")
ax_time.set_ylabel("Amp")
ax_time.margins(x=0)

# 2. OUTPUT KEDUA: Global FFT (Konversi DFT)
ax_global.plot(freqs, amps, color='blue', linewidth=0.8)
ax_global.set_title("2. Global Frequency (Konversi DFT Total)")
ax_global.set_ylabel("Magnitude")
ax_global.grid(True, alpha=0.3)

# 3. OUTPUT KETIGA: Analisis FFT (Placeholder Awal)
ax_local.text(0.5, 0.5, "KLIK PADA SPEKTROGRAM (GRAFIK 4)\nUNTUK MELIHAT ANALISIS FFT DI SINI", 
              ha='center', va='center', transform=ax_local.transAxes, color='gray')
ax_local.set_title("3. Analisis FFT Lokal (Interaktif)")
ax_local.set_ylabel("Magnitude")
ax_local.grid(True, alpha=0.3)

# 4. OUTPUT KEEMPAT: Spektrogram + Jejak Dominan
pcm = ax_spec.pcolormesh(t_spec, f_spec, 10 * np.log10(Sxx + 1e-10), 
                         shading='auto', cmap='viridis')
# Garis merah jejak dominan
ax_spec.plot(t_spec, dom_freqs, color='red', linestyle='--', linewidth=1, alpha=0.8, label='Dominan Trace')
ax_spec.legend(loc='upper right', fontsize='small')

ax_spec.set_title("4. Spektrogram (Klik untuk Analisis)")
ax_spec.set_ylabel("Freq [Hz]")
ax_spec.set_xlabel("Time [s]")

fig.colorbar(pcm, ax=ax_spec, orientation='vertical', label='dB')
fig.canvas.mpl_connect('button_press_event', on_click)

plt.show()
