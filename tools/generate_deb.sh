TMP_DIR="/tmp/ytdlg_gen_deb_tmp/"
TGT_PKG="${TMP_DIR}output/"

rm -rf ${TMP_DIR}
mkdir ${TMP_DIR}
wheel2deb -x dist/ --depends ffmpeg gettext python3-pubsub python3-twodict python3-wxgtk4.0 --name youtube-dlg -o ${TMP_DIR}output/
TGT_PKG=${TGT_PKG}`ls ${TGT_PKG}`
cp tools/youtube-dlg.desktop ${TGT_PKG}/src/
echo -e "\nsrc/youtube-dlg.desktop /usr/share/applications/" >> ${TGT_PKG}/debian/install
sed -e "s/wheel2deb <wheel2deb@upciti.com>/kazuto28 <mountaindull@gmail.com>/g" -i ${TGT_PKG}/debian/control -i ${TGT_PKG}/debian/changelog
wheel2deb build -p ${TMP_DIR}output/
cp ${TMP_DIR}output/*.deb packages/
