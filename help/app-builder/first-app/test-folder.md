---
title: The test folder
description: Learn about the types of files in the test folder for this sample application
landing-page-description: Learn about Adobe Developer App Builder used with Adobe Commerce and what types of files are located in the test folder
kt: 12424
doc-type: tutorial
audience: all
last-substantial-update: 2023-03-3

---

# test folder

The test folder for this sample app contains a single JavaScript file. This is used when running unit tests on the application

This is a simple example and can be expanded to do x, y, and z.

## Who is this video for?

* Developers new to Adobe Commerce with limited experience with Adobe App Builder who is learning about the test folder.

## Video content

* Why create the .env file
* Limitations
* How it is used in the application

>[!VIDEO](https://video.tv.adobe.com/v/xxxxxxxx)

## Code Samples

test/utils.test.js

```javascript
/* 
* <license header>
*/

const utils = require('./../actions/utils.js')

test('interface', () => {
  expect(typeof utils.errorResponse).toBe('function')
  expect(typeof utils.stringParameters).toBe('function')
  expect(typeof utils.checkMissingRequestInputs).toBe('function')
  expect(typeof utils.getBearerToken).toBe('function')
})

describe('errorResponse', () => {
  test('(400, errorMessage)', () => {
    const res = utils.errorResponse(400, 'errorMessage')
    expect(res).toEqual({
      error: {
        statusCode: 400,
        body: { error: 'errorMessage' }
      }
    })
  })

  test('(400, errorMessage, logger)', () => {
    const logger = {
      info: jest.fn()
    }
    const res = utils.errorResponse(400, 'errorMessage', logger)
    expect(logger.info).toHaveBeenCalledWith('400: errorMessage')
    expect(res).toEqual({
      error: {
        statusCode: 400,
        body: { error: 'errorMessage' }
      }
    })
  })
})

describe('stringParameters', () => {
  test('no auth header', () => {
    const params = {
      a: 1, b: 2, __ow_headers: { 'x-api-key': 'fake-api-key' }
    }
    expect(utils.stringParameters(params)).toEqual(JSON.stringify(params))
  })
  test('with auth header', () => {
    const params = {
      a: 1, b: 2, __ow_headers: { 'x-api-key': 'fake-api-key', authorization: 'secret' }
    }
    expect(utils.stringParameters(params)).toEqual(expect.stringContaining('"authorization":"<hidden>"'))
    expect(utils.stringParameters(params)).not.toEqual(expect.stringContaining('secret'))
  })
})

describe('checkMissingRequestInputs', () => {
  test('({ a: 1, b: 2 }, [a])', () => {
    expect(utils.checkMissingRequestInputs({ a: 1, b: 2 }, ['a'])).toEqual(null)
  })
  test('({ a: 1 }, [a, b])', () => {
    expect(utils.checkMissingRequestInputs({ a: 1 }, ['a', 'b'])).toEqual('missing parameter(s) \'b\'')
  })
  test('({ a: { b: { c: 1 } }, f: { g: 2 } }, [a.b.c, f.g.h.i])', () => {
    expect(utils.checkMissingRequestInputs({ a: { b: { c: 1 } }, f: { g: 2 } }, ['a.b.c', 'f.g.h.i'])).toEqual('missing parameter(s) \'f.g.h.i\'')
  })
  test('({ a: { b: { c: 1 } }, f: { g: 2 } }, [a.b.c, f.g.h])', () => {
    expect(utils.checkMissingRequestInputs({ a: { b: { c: 1 } }, f: { g: 2 } }, ['a.b.c', 'f'])).toEqual(null)
  })
  test('({ a: 1, __ow_headers: { h: 1, i: 2 } }, undefined, [h])', () => {
    expect(utils.checkMissingRequestInputs({ a: 1, __ow_headers: { h: 1, i: 2 } }, undefined, ['h'])).toEqual(null)
  })
  test('({ a: 1, __ow_headers: { f: 2 } }, [a], [h, i])', () => {
    expect(utils.checkMissingRequestInputs({ a: 1, __ow_headers: { f: 2 } }, ['a'], ['h', 'i'])).toEqual('missing header(s) \'h,i\'')
  })
  test('({ c: 1, __ow_headers: { f: 2 } }, [a, b], [h, i])', () => {
    expect(utils.checkMissingRequestInputs({ c: 1 }, ['a', 'b'], ['h', 'i'])).toEqual('missing header(s) \'h,i\' and missing parameter(s) \'a,b\'')
  })
  test('({ a: 0 }, [a])', () => {
    expect(utils.checkMissingRequestInputs({ a: 0 }, ['a'])).toEqual(null)
  })
  test('({ a: null }, [a])', () => {
    expect(utils.checkMissingRequestInputs({ a: null }, ['a'])).toEqual(null)
  })
  test('({ a: \'\' }, [a])', () => {
    expect(utils.checkMissingRequestInputs({ a: '' }, ['a'])).toEqual('missing parameter(s) \'a\'')
  })
  test('({ a: undefined }, [a])', () => {
    expect(utils.checkMissingRequestInputs({ a: undefined }, ['a'])).toEqual('missing parameter(s) \'a\'')
  })
})

describe('getBearerToken', () => {
  test('({})', () => {
    expect(utils.getBearerToken({})).toEqual(undefined)
  })
  test('({ authorization: Bearer fake, __ow_headers: {} })', () => {
    expect(utils.getBearerToken({ authorization: 'Bearer fake', __ow_headers: {} })).toEqual(undefined)
  })
  test('({ authorization: Bearer fake, __ow_headers: { authorization: fake } })', () => {
    expect(utils.getBearerToken({ authorization: 'Bearer fake', __ow_headers: { authorization: 'fake' } })).toEqual(undefined)
  })
  test('({ __ow_headers: { authorization: Bearerfake} })', () => {
    expect(utils.getBearerToken({ __ow_headers: { authorization: 'Bearerfake' } })).toEqual(undefined)
  })
  test('({ __ow_headers: { authorization: Bearer fake} })', () => {
    expect(utils.getBearerToken({ __ow_headers: { authorization: 'Bearer fake' } })).toEqual('fake')
  })
  test('({ __ow_headers: { authorization: Bearer fake Bearer fake} })', () => {
    expect(utils.getBearerToken({ __ow_headers: { authorization: 'Bearer fake Bearer fake' } })).toEqual('fake Bearer fake')
  })
})

```

{{$include /help/_includes/app-builder-first-app-related-links.md}}