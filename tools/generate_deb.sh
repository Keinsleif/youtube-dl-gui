TMP_DIR="/tmp/ytdlg_gen_deb_tmp/"
TGT_PKG="${TMP_DIR}output/"

rm -rf ${TMP_DIR}
mkdir ${TMP_DIR}
python3 setup.py bdist_wheel
wheel2deb dist/*.whl --depends ffmpeg gettext python3-pubsub python3-twodict python3-wxgtk4.0 --name youtube-dlg -o ${TMP_DIR}output/ -c tools/wheel2deb.yml
TGT_PKG=${TGT_PKG}`ls ${TGT_PKG}`
cp tools/youtube-dlg.desktop ${TGT_PKG}/src/
echo -e "\nsrc/youtube-dlg.desktop /usr/share/applications/" >> ${TGT_PKG}/debian/install
wheel2deb build -p ${TMP_DIR}output/
cp ${TMP_DIR}output/*.deb packages/
rm -rf ${TMP_DIR}
