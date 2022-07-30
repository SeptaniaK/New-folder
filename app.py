import pandas as pd
# import plotly.express as px
import streamlit as st
# import plotly.graph_objects as go

st.title("Dashboard Data Penindakan Lalu Lintas Bulan Januari")
st.markdown("dashboard ini akan membantu pengguna untuk memahami data dan outputnya")
st.sidebar.title("Pilih Visual Charts")

data = pd.read_csv('data_lalulintas.csv')
st.dataframe(data)
st.markdown("a. Periksa bentuk data (jumlah baris dan kolom)")
data.shape
st.markdown("b. Menampilkan list kolom")
data.columns

sort = st.selectbox('Urutkan secara',
					('Ascending', 'Descending'))
selected = st.selectbox('Pilih',
								options= ['bap_tilang', 'stop_operasi', 'bap_polisi', 'stop_operasi_polisi', 'penderekan', 
								'ocp_roda_dua', 'ocp_roda_empat', 'angkut_motor'])
if sort == 'Ascending':
	if selected == 'bap_tilang':
		s = data.bap_tilang.sort_values(ascending=1)
		s
	elif selected == 'stop_operasi':
		s = data.stop_operasi.sort_values(ascending=1)
		s
	elif selected == 'bap_polisi':
		s = data.bap_polisi.sort_values(ascending=1)
		s
	elif selected == 'stop_operasi_polisi':
		s = data.stop_operasi_polisi.sort_values(ascending=1)
		s
	elif selected == 'penderekan':
		s = data.penderekan.sort_values(ascending=1)
		s
	elif selected == 'ocp_roda_dua':
		s = data.ocp_roda_dua.sort_values(ascending=1)
		s
	elif selected == 'ocp_roda_empat':
		s = data.ocp_roda_empat.sort_values(ascending=1)
		s
	elif selected == 'angkut_motor':
		s = data.angkut_motor.sort_values(ascending=1)
		s
elif sort == 'Descending':
	if selected == 'bap_tilang':
		s = data.bap_tilang.sort_values(ascending=0)
		s
	elif selected == 'stop_operasi':
		s = data.stop_operasi.sort_values(ascending=0)
		s
	elif selected == 'bap_polisi':
		s = data.bap_polisi.sort_values(ascending=0)
		s
	elif selected == 'stop_operasi_polisi':
		s = data.stop_operasi_polisi.sort_values(ascending=0)
		s
	elif selected == 'penderekan':
		s = data.penderekan.sort_values(ascending=0)
		s
	elif selected == 'ocp_roda_dua':
		s = data.ocp_roda_dua.sort_values(ascending=0)
		s
	elif selected == 'ocp_roda_empat':
		s = data.ocp_roda_empat.sort_values(ascending=0)
		s
	elif selected == 'angkut_motor':
		s = data.angkut_motor.sort_values(ascending=0)
		s

chart_visual = st.sidebar.selectbox('Pilih jenis Charts/Plot',
									('Line Chart', 'Bar Chart', 'Bubble Chart', 'Box Plot'))

selected_status = st.sidebar.selectbox('Pilih Penindakan',
									options = ['bap_tilang', 'stop_operasi', 'bap_polisi', 'stop_operasi_polisi', 'penderekan', 
									'ocp_roda_dua', 'ocp_roda_empat', 'angkut_motor'])

fig = go.Figure()

st.title("Chart")
if chart_visual == 'Line Chart':
	if selected_status == 'bap_polisi':
		fig.add_trace(go.Scatter(x = data.wilayah, y = data.bap_polisi,
								mode = 'lines',))
	if selected_status == 'bap_tilang':
		fig.add_trace(go.Scatter(x = data.wilayah, y = data.bap_tilang,
								mode = 'lines'))
	if selected_status == 'stop_operasi':
		fig.add_trace(go.Scatter(x = data.wilayah, y = data.stop_operasi,
								mode = 'lines'))
	if selected_status == 'stop_operasi_polisi':
		fig.add_trace(go.Scatter(x = data.wilayah, y = data.stop_operasi_polisi,
								mode = 'lines'))
	if selected_status == 'penderekan':
		fig.add_trace(go.Scatter(x = data.wilayah, y = data.penderekan,
								mode = 'lines'))
	if selected_status == 'ocp_roda_dua':
		fig.add_trace(go.Scatter(x = data.wilayah, y = data.ocp_roda_dua,
								mode = 'lines'))
	if selected_status == 'ocp_roda_empat':
		fig.add_trace(go.Scatter(x = data.wilayah, y = data.ocp_roda_empat,
								mode = 'lines'))
	if selected_status == 'angkut_motor':
		fig.add_trace(go.Scatter(x = data.wilayah, y = data.angkut_motor,
								mode = 'lines'))
			

elif chart_visual == 'Bar Chart':
	if selected_status == 'bap_polisi':
		fig.add_trace(go.Bar(x=data.wilayah, y=data.bap_polisi))
	if selected_status == 'bap_tilang':
		fig.add_trace(go.Bar(x=data.wilayah, y=data.bap_tilang))
	if selected_status == 'stop_operasi':
		fig.add_trace(go.Bar(x=data.wilayah, y=data.stop_operasi))
	if selected_status == 'stop_operasi_polisi':
		fig.add_trace(go.Bar(x=data.wilayah, y=data.stop_operasi_polisi))
	if selected_status == 'penderekan':
		fig.add_trace(go.Bar(x=data.wilayah, y=data.penderekan))
	if selected_status == 'ocp_roda_dua':
		fig.add_trace(go.Bar(x=data.wilayah, y=data.ocp_roda_dua))
	if selected_status == 'ocp_roda_empat':
		fig.add_trace(go.Bar(x=data.wilayah, y=data.ocp_roda_empat))
	if selected_status == 'angkut_motor':
		fig.add_trace(go.Bar(x=data.wilayah, y=data.angkut_motor))
	
elif chart_visual == 'Bubble Chart':
	if selected_status == 'bap_polisi':
		fig.add_trace(go.Scatter(x=data.wilayah,
								y=data.bap_polisi,
								mode='markers',
								marker_size=[40, 60, 80, 60, 40, 50]))
	if selected_status == 'bap_tilang':
		fig.add_trace(go.Scatter(x=data.wilayah, y=data.bap_tilang,
								mode='markers',
								marker_size=[40, 60, 80, 60, 40, 50]))
	if selected_status == 'stop_operasi':
		fig.add_trace(go.Scatter(x=data.wilayah,
								y=data.stop_operasi,
								mode='markers',
								marker_size=[40, 60, 80, 60, 40, 50]))
	if selected_status == 'stop_operasi_polisi':
		fig.add_trace(go.Scatter(x=data.wilayah,
								y=data.stop_operasi_polisi,
								mode='markers',
								marker_size=[40, 60, 80, 60, 40, 50]))
	if selected_status == 'penderekan':
		fig.add_trace(go.Scatter(x=data.wilayah,
								y=data.penderekan,
								mode='markers',
								marker_size=[40, 60, 80, 60, 40, 50]))
	if selected_status == 'ocp_roda_dua':
		fig.add_trace(go.Scatter(x=data.wilayah,
								y=data.ocp_roda_dua,
								mode='markers',
								marker_size=[40, 60, 80, 60, 40, 50]))
	if selected_status == 'ocp_roda_empat':
		fig.add_trace(go.Scatter(x=data.wilayah,
								y=data.ocp_roda_empat,
								mode='markers',
								marker_size=[40, 60, 80, 60, 40, 50]))
	if selected_status == 'angkut_motor':
		fig.add_trace(go.Scatter(x=data.wilayah,
								y=data.angkut_motor,
								mode='markers',
								marker_size=[40, 60, 80, 60, 40, 50]))
	
elif chart_visual == 'Box Plot':
	if selected_status == 'bap_polisi':
		fig.add_trace(go.Box(x=data.wilayah, y=data.bap_polisi))
	if selected_status == 'bap_tilang':
		fig.add_trace(go.Box(x=data.wilayah, y=data.bap_tilang))
	if selected_status == 'stop_operasi':
		fig.add_trace(go.Box(x=data.wilayah, y=data.stop_operasi))
	if selected_status == 'stop_operasi_polisi':
		fig.add_trace(go.Box(x=data.wilayah, y=data.stop_operasi_polisi))
	if selected_status == 'penderekan':
		fig.add_trace(go.Box(x=data.wilayah, y=data.penderekan))
	if selected_status == 'ocp_roda_dua':
		fig.add_trace(go.Box(x=data.wilayah, y=data.ocp_roda_dua))
	if selected_status == 'ocp_roda_empat':
		fig.add_trace(go.Box(x=data.wilayah, y=data.ocp_roda_empat))
	if selected_status == 'angkut_motor':
		fig.add_trace(go.Box(x=data.wilayah, y=data.angkut_motor))
	
st.plotly_chart(fig, use_container_width=True)
