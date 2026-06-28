import streamlit as st

st.title("📋 Menaxhimi i Detyrave")


if "detyrat" not in st.session_state:
    st.session_state.detyrat = []


detyre_e_re = st.text_input("Shkruaj detyrën e re:")

if st.button("Shto Detyrën"):
    if detyre_e_re.strip() == "":
        st.warning("Shkruaj një detyrë para se ta shtosh.")
    else:
        st.session_state.detyrat.append({
            "pershkrim": detyre_e_re,
            "perfunduar": False
        })
        st.success("Detyra u shtua!")

st.divider()


if len(st.session_state.detyrat) == 0:
    st.info("Nuk ka detyra ende. Shto një detyrë!")
else:
    st.subheader("Lista e Detyrave")
    for i, detyre in enumerate(st.session_state.detyrat):
        col1, col2, col3 = st.columns([0.1, 0.7, 0.2])

     
        with col1:
            e_kryer = st.checkbox(
                "",
                value=detyre["perfunduar"],
                key=f"check_{i}"
            )
            st.session_state.detyrat[i]["perfunduar"] = e_kryer

      
        with col2:
            if e_kryer:
                st.markdown(f"~~{detyre['pershkrim']}~~")
            else:
                st.write(detyre["pershkrim"])

   
        with col3:
            if st.button("🗑️ Fshi", key=f"fshi_{i}"):
                st.session_state.detyrat.pop(i)
                st.rerun()