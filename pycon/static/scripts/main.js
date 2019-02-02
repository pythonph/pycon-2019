import 'babel-polyfill'
import Parallax from 'parallax-js'
import tippy from 'tippy.js'

new Parallax(document.querySelector('#scene_1'));
new Parallax(document.querySelector('#scene_2'));

document.querySelectorAll('.sponsors-list__sponsor').forEach(el => {
  const img = el.querySelector('img');
  const description = el.querySelector('.tooltip-box__wrapper');

  tippy(img, {
    animateFill: false,
    animation: 'fade',
    arrow: true,
    content: description,
    interactive: true,
    performance: true,
    placement: 'top',
    size: 'large',
  })
})
