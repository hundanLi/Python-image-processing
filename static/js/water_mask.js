function mask_type(obj, val) {
    $(".mask-type").hide();
    if (val === 'text') {
        $(".text").show();

    } else {
        $(".logo").show();
    }
}
