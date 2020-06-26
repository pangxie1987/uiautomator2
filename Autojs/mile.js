
//秘乐短视频邀请码：55729056

auto.waitFor();
app.launchApp('秘乐短视频');
sleep(8000);
console.show();
let i = 1;
let see_count = 500;
while (true) {
    toast("秘乐短视频滑动" + i + '次' + "总计:" + see_count + "次")
    console.log("秘乐短视频滑动" + i + '次' + "总计:" + see_count + "次");
    randomHeart();
    slideScreenDown(303, 1328, 335, 171, 600);
    i++;
    if (i == 500) {
        home();
        exit();
    }
}
/**
 * 屏幕向下滑动并延迟8至12秒
 */
function slideScreenDown(startX, startY, endX, endY, pressTime) {
    swipe(startX, startY, endX, endY, pressTime);
    let delayTime = random(8000, 12000);
    sleep(delayTime);
}
/**随机点赞并休息一秒 */
function randomHeart() {
    index = random(1, 100);
    if (index == 66) {
        var target = id('ly_video_item_like').findOnce();
        if (target == null) {
            return;
        } else {
            target.click();
            sleep(1000);
        }
    }
}
