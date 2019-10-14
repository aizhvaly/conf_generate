
var syncList1 = new syncList;

syncList1.dataList = {
/* 1 --> 2 */
  'PVL/':{
      '':'-',
      'NN/':'Нижегородская'
  },/*,

  'URAL/':{
      '':'-',
      'EKB/':'Свердловская'
  },*/

/* 2 --> 3 */

  'NN/':{
      '':'-',
      'Nnov/':'Нижний Новгород',
      "Arz/": 'Арзамас',
      "Bor/": 'Бор'
  },/*
  'EKB/':{
      '':'-',
      'D-link/':'D-link',
      'Huawei/':'Huawei'
  },
/* 3 --> 4 */
  'Nnov/':{
    '':'-',
    'D-link/': 'D-link',
    'Huawei/': 'Huawei'
  },
  'Arz/':{
    '':'-',
    'D-link/': 'D-link'/*,
    'Huawei/': 'Huawei'*/
  },
  'Bor/':{
    '':'-',
    'D-link/': 'D-link',
    'Huawei/': 'Huawei'
  },

/* 4 --> 5 */

  'D-link/': {
    '':'-',
    'DES-1210-28/':'DES-1210-28/ME',
    'DES-1228/':'DES-1228/ME',
    'DES-3200-52/':'DES-3200-52'
  },
  'Huawei/': {
    '':'-',
    'S2326TP-EI/':'S2326TP-EI',
    'S2352P-EI/':'S2352P-EI'
  }

};

syncList1.sync("dir0","dir1","dir2","dir3","dir4");
