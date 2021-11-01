mkdir -p ˜/.streamlit/

echo "\
[0.0.0.0]\n\
port = 80\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ˜/.streamlit/config.toml
